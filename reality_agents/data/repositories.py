from database import get_session
from models import Game

# repository implementations are classes that encapsulate the logic required to access data sources
# you should only define one repository for each aggregate root

class GameRepository:
    def __init__(self):
        self.session = get_session()

    def get_game_by_id(self, game_id):
        return self.session.query(Game).filter_by(id=game_id).first()

    def add_game(self, game):
        self.session.add(game)
        self.session.commit()


