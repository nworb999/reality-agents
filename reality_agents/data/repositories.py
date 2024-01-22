from database import get_session
from models import Game

# placeholder -- repository is for abstracting the data layer

class GameRepository:
    def __init__(self):
        self.session = get_session()

    def get_game_by_id(self, game_id):
        return self.session.query(Game).filter_by(id=game_id).first()

    def add_game(self, game):
        self.session.add(game)
        self.session.commit()


