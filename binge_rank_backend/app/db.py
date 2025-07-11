from databases import Database
import sqlalchemy
import os


database: Database = None  # global placeholder

def init(db_instance: Database):
    global database
    database = db_instance
 
# SQLAlchemy metadata for table definitions (optional)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "br_user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
)
