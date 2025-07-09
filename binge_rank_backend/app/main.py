from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "BingeRank API is up and running!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello, World!"}