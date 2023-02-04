from fastapi import FastAPI

app = FastAPI()

@app.get("/msg")
def read_root():
    return {"Hello": "World"}