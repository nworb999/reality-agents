from reality_agents.servers.game_server.server import GameServer

if __name__ == "__main__":
    from reality_agents.data.models import Base
    from reality_agents.data.database import engine
    Base.metadata.create_all(engine)

    game_server = GameServer()
    game_server.start_game()
