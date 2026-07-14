from fastapi import FastAPI
import uvicorn

app_3=FastAPI()

@app_3.get("/")
def read_root():
    return({'message':'API_3 running'})
@app_3.get('/i Have built a functioning API')
def build_api():
    return{'message':'Functioning api'}