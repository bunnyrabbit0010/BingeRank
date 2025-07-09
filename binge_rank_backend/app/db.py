# app/db.py

from databases import Database
import sqlalchemy
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# Create an async database connection
database = Database(DATABASE_URL)

# Metadata and table definition (optional but helpful)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "br_user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
)
