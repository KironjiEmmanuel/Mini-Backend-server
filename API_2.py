from fastapi import FastAPI
import uvicorn

app= FastAPI()

@app.get("/")
def read_root():
  return {"message": "API running"}

@app.get("/THE API IS RUNNING")
def read_the_api_is_running():
    return {"message": "THE API IS RUNNING"}
