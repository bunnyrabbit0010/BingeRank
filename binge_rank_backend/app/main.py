
# app/main.py

from fastapi import FastAPI
from app.db import database, users
from dotenv import load_dotenv
import os

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")


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
