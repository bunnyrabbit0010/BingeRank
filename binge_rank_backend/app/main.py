
# app/main.py

from fastapi import FastAPI
import pg8000.native
import ssl
from urllib.parse import urlparse
from dotenv import load_dotenv
from databases import Database
import os
from app.db import users

# Load environment variables from .env
load_dotenv()

# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the Database object
database = Database(DATABASE_URL)

# Import and pass database to other modules
from . import db
db.init(database)  # <-- inject the instance


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




