import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'postgresql://blog_user:thanhkhon123@localhost:5432/blog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
