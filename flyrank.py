from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get("/")
def read_root():
  return {"message": "Hello"}

@app.get("/status")
def read_status():
  return {"message": "status"}