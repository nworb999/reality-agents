# main.py
from src.data.repositories import GameRepository
from src.servers.agent_server.server import start_agent_server
from src.servers.environment_server.server import start_environment_server
from src.servers.game_server.server import start_game_server

if __name__ == "__main__":
    # Initialize the data layer (e.g., connecting to the database, creating tables)
    from src.data.models import Base
    from src.data.database import engine
    Base.metadata.create_all(engine)

    # Example of using the data layer
    game_repository = GameRepository()
    game = game_repository.get_game_by_id(1)
    if game:
        print(f"Game found: {game.name}")
    else:
        print("Game not found, starting servers...")

    # Start the servers
    start_agent_server()
    start_environment_server()
    start_game_server()
