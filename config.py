import os

DB_USERNAME = "root"
DB_PASSWORD = "root"
DB_HOST = "mysql-container"  # Use container name
DB_NAME = "chat"

SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False