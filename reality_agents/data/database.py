from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from reality_agents.data.models import Base

DATABASE_URL = "sqlite:///reality_agents/data/memory.db"

CLEAR_DB = True

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db(clear_db=False):
    if clear_db:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def setup_db():
    init_db(clear_db=CLEAR_DB)
    print(f"Database initialized.")
    print(f"clear_db set to {CLEAR_DB}.")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
