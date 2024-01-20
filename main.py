from src.servers.game_server.server import GameServer

if __name__ == "__main__":
    from src.data.models import Base
    from src.data.database import engine
    Base.metadata.create_all(engine)

    game_server = GameServer()
    game_server.start_game()
