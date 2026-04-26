from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS
import pandas as pd
import joblib
import os

modelo = joblib.load(os.path.join(os.path.dirname(__file__), 'modelo_catboost.pkl'))

variables_originales = [
    'duration_ms', 'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
    'explicit', 'key', 'mode', 'time_signature',
    'artists', 'album_name', 'track_name', 'track_genre'
]
variables_categoricas = ['artists', 'album_name', 'track_name', 'track_genre']

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='API de Popularidad Spotify',
          description='Prediccion de popularidad con CatBoost', doc='/docs')

ns = api.namespace('predict', description='Operaciones de prediccion')

entrada_modelo = api.model('EntradaModelo', {
    var: fields.String(required=True) if var in variables_categoricas
    else fields.Float(required=True)
    for var in variables_originales
})

@ns.route('/')
class Prediccion(Resource):
    @ns.expect(entrada_modelo)
    def post(self):
        datos = [request.json[var] for var in variables_originales]
        df = pd.DataFrame([datos], columns=variables_originales)
        pred = modelo.predict(df)[0]
        return {'popularidad_estimada': round(float(pred), 2)}, 200

@ns.route('/params')
class PrediccionConParametros(Resource):
    def get(self):
        try:
            datos = [
                request.args.get(var) if var in variables_categoricas
                else float(request.args.get(var, 0))
                for var in variables_originales
            ]
            df = pd.DataFrame([datos], columns=variables_originales)
            pred = modelo.predict(df)[0]
            return {'popularidad_estimada': round(float(pred), 2)}, 200
        except Exception as e:
            return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='0.0.0.0', port=5000)
