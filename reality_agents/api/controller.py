from reality_agents.services.game.game_service import (
    ConversationService as GameService,
)
from contextlib import contextmanager
from reality_agents.data.database import get_db, setup_db


# handles game logic
# return messages with status codes for when it's FINISHED


@contextmanager
def initialize_db_session(test_flag=False):
    setup_db(test_flag)
    db_session_gen = get_db()
    db = next(db_session_gen)
    try:
        yield db
    finally:
        next(db_session_gen, None)


class GameController:
    def __init__(self, characters, conflict, scene, test_flag=False):
        with initialize_db_session(test_flag) as db:
            self.game_service = GameService(
                characters=characters,
                conflict=conflict,
                scene=scene,
                test_flag=test_flag,
                db=db,
            )

    def start_game(self):
        response = self.game_service.start_game()
        return {"message": response}

    def update(self):
        game_status = self.game_service.update()
        if game_status["status"] == "Game over: conversation ended":
            return {"message": "Game over: conversation ended"}
        if game_status["status"] == "Game over: cutoff reached":
            return {"message": "Game over: cutoff reached"}
        return {"message": game_status}
