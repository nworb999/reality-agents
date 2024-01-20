# src/data/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# An example connection string to a SQLite database
DATABASE_URI = 'sqlite:///mydatabase.db'

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
