# Mini Backend

Minimal FastAPI server with two JSON endpoints.

## Run it
pip install -r requirements.txt
uvicorn flyrank:app --reload

## Endpoints
- GET /       -> {"message": "Hello"}
- GET /status -> {"message": "status"}