from reality_agents.data.models import Memory
from datetime import datetime
from sqlalchemy.orm import Session

# crud operations


def create_memory_entry(
    session: Session,
    game_id: str,
    conversation_id: str,
    round_id: str,
    turn_id: str,
    speaker_id: str,
    directed_at_id: str,
    statement: str,
):
    new_entry = Memory(
        game_id=game_id,
        conversation_id=conversation_id,
        round_id=round_id,
        turn_id=turn_id,
        speaker_id=speaker_id,
        directed_at_id=directed_at_id,
        statement=statement,
    )

    session.add(new_entry)
    session.commit()
    session.refresh(new_entry)
    return new_entry


def update_last_accessed(session: Session, memory_id: int):
    entry = session.query(Memory).filter(Memory.id == memory_id).first()
    if entry:
        entry.last_accessed = datetime.utcnow()
        session.commit()


def get_memory_entries(session: Session, game_id: str):
    # currently updating all last accessed
    entries = session.query(Memory).filter(Memory.game_id == game_id).all()
    for entry in entries:
        entry.last_accessed = datetime.utcnow()
    session.commit()
    return entries
