
# app/main.py

from fastapi import FastAPI
from app.db import database, users

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"message": "BingeRank API is up and running!"}

@app.get("/users")
async def get_users():
    query = users.select()
    results = await database.fetch_all(query)
    return results
