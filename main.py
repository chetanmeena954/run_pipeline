from fastapi import FastAPI
from data import run_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Ankita is running API test"}

@app.get("/top-products")
def get_data():
    data = run_pipeline()
    return data.to_dict()