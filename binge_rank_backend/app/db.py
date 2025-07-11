from databases import Database
import sqlalchemy
import os

# Use the transaction pooler URL from environment for IPv4 compatibility
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres.tfsagqekvebxrbjxxdhe:FSacOoliZZbDqgYv@aws-0-us-east-2.pooler.supabase.com:6543/postgres"
)

database: Database = None  # global placeholder

def init(db_instance: Database):
    global database
    database = db_instance
 
# Create an async database connection instance
# database = Database(DATABASE_URL)

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
