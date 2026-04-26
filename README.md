# API de Predicción de Popularidad Spotify

API REST construida con Flask-RESTX que predice la popularidad de canciones
usando un modelo CatBoostRegressor entrenado con el dataset de Spotify.

## Endpoints
- `POST /predict/` — JSON con 18 variables de audio
- `GET /predict/params` — Query parameters
- `GET /docs` — Swagger UI

## Variables de entrada
[ver documentación completa]

## Instalación local
pip install -r requirements.txt
python api.py
