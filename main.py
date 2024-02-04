from utils.constants import ASCII_INTRO, VALID_GAME_TYPES
from reality_agents.data.database import init_db, get_db
from reality_agents.data.repository import create_memory_entry, get_memory_entries
from reality_agents.view.game_handlers import (
    play_horse_race_game,
    play_conversation_game,
)


def create_seed_data():
    init_db()
    db = next(get_db())

    create_memory_entry(
        db,
        "game1",
        "conv1",
        "round1",
        "turn1",
        "speaker1",
        None,
        "This is the first test statement.",
    )
    create_memory_entry(
        db,
        "game1",
        "conv2",
        "round2",
        "turn2",
        "speaker2",
        "speaker1",
        "This is the second test statement.",
    )

    db.close()


def retrieve_data():
    db = next(get_db())

    entries = get_memory_entries(db, "game1")

    for entry in entries:
        print(f"ID: {entry.id}, Statement: {entry.statement}")

    db.close()


def main():
    game_type = input("Please enter the game type: ").lower().strip() or "convo"

    if game_type in ["conversation", "convo"]:
        play_conversation_game()
    elif game_type == "horse race":
        play_horse_race_game()
    elif game_type not in VALID_GAME_TYPES:
        print("Unknown game type. Exiting.")


if __name__ == "__main__":
    print("\033[2J\033[H", end="")
    print(ASCII_INTRO)

    init_db()
    print("Database initialized.")

    create_seed_data()
    print("Database seeded.")

    retrieve_data()

    main()
