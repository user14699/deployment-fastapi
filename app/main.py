from fastapi import FastAPI

app = FastAPI(title="My FastAPI Project")

@app.get("/")
def home():
    return {"message": "Kundan FastAPI Project Running with Docker and Pipelines"}