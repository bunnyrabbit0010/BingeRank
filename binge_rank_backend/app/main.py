
# app/main.py

from fastapi import FastAPI
import pg8000.native
import ssl
from urllib.parse import urlparse
from app.db import database, users
#from dotenv import load_dotenv
#import os

#load_dotenv()
#TMDB_API_KEY = os.getenv("TMDB_API_KEY")



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


# Parse the URL
url = "postgresql://postgres.tfsagqekvebxrbjxxdhe:FSacOoliZZbDqgYv@aws-0-us-east-2.pooler.supabase.com:6543/postgres"
result = urlparse(url)
@app.get("/checkdb")
def check_db():
    print("Checking database connection...")

    conn = pg8000.native.Connection(
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port,
        database=result.path.lstrip("/"),
        ssl_context = ssl._create_unverified_context()
    )

    print("✅ Connected. Server time:", conn.run("SELECT current_timestamp;"))
    conn.close()
    print("✅ Connection successful")



@app.get("/users")
async def get_users():
    query = users.select()
    results = await database.fetch_all(query)
    return results




