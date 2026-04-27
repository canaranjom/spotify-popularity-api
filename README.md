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

Ejemplos:

{
  "duration_ms": 200000,
  "danceability": 0.65,
  "energy": 0.72,
  "loudness": -6.5,
  "speechiness": 0.045,
  "acousticness": 0.12,
  "instrumentalness": 0.0,
  "liveness": 0.11,
  "valence": 0.58,
  "tempo": 120.5,
  "explicit": 0,
  "key": 5,
  "mode": 1,
  "time_signature": 4,
  "artists": "Bad Bunny",
  "album_name": "Un Verano Sin Ti",
  "track_name": "Tití Me Preguntó",
  "track_genre": "latin"
}


{
  "duration_ms": 212000,
  "danceability": 0.83,
  "energy": 0.78,
  "loudness": -5.2,
  "speechiness": 0.08,
  "acousticness": 0.04,
  "instrumentalness": 0.0,
  "liveness": 0.12,
  "valence": 0.76,
  "tempo": 94.0,
  "explicit": 0,
  "key": 7,
  "mode": 0,
  "time_signature": 4,
  "artists": "Reykon",
  "album_name": "El Besito",
  "track_name": "El Besito",
  "track_genre": "reggaeton"
}


## Instalación local
pip install -r requirements.txt
python api.py
