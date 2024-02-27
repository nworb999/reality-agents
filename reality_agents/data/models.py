from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

Base = declarative_base()


class Memory(Base):
    __tablename__ = "memory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.utcnow)
    last_accessed = Column(DateTime, default=datetime.utcnow)
    game_id = Column(String(50), nullable=False)
    conversation_id = Column(String(50), nullable=False)
    round_id = Column(String(50), nullable=False)
    turn_id = Column(String(50), nullable=False)
    speaker_id = Column(String(50), nullable=False)
    directed_at_id = Column(String(50), nullable=True)
    statement = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Memory(id={self.id}, game_id={self.game_id}, last_accessed={self.last_accessed}, statement={self.statement})>"
