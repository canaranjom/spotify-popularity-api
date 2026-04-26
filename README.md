# API de Predicción de Popularidad Spotify

API REST construida con Flask-RESTX que predice la popularidad de canciones
usando un modelo CatBoostRegressor entrenado con el dataset de Spotify.

## Endpoints
- `POST /predict/` — JSON con 18 variables de audio
- `GET /predict/params` — Query parameters
- `GET /docs` — Swagger UI

## Variables de entrada
{
  "duration_ms": 0,
  "danceability": 0,
  "energy": 0,
  "loudness": 0,
  "speechiness": 0,
  "acousticness": 0,
  "instrumentalness": 0,
  "liveness": 0,
  "valence": 0,
  "tempo": 0,
  "explicit": 0,
  "key": 0,
  "mode": 0,
  "time_signature": 0,
  "artists": "string",
  "album_name": "string",
  "track_name": "string",
  "track_genre": "string"
}



## Instalación local
pip install -r requirements.txt
python api.py
