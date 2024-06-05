import re
from reality_agents.services.llm.handler import get_response

LIST_OF_SCENES = []
LIST_OF_CONFLICTS = []
LIST_OF_NAMES = []


def format_character_name_response(character_response):
    match = re.search(r"[Nn]ame:\s*(.*)", character_response)
    if match:
        return match.group(1).strip()
    else:
        return (
            character_response.strip()
            .replace("Sure! How about the name", "")
            .replace("?", "")
            .replace("**", "")
        )


def generate_cuttlefish_scenario():
    scene = get_response(
        prompt=f"please generate in one or two words only a random setting for a reality TV show. {' Please do not use any of the following: [' + ', '.join(LIST_OF_SCENES) + ']' if LIST_OF_SCENES else ''}"
    ).replace('"', "")
    LIST_OF_SCENES.append(scene)
    conflict = get_response(
        prompt=f"please generate in one or two words only a conflict for a reality TV show given setting: {scene}.  {' Please do not use any of the following: [' + ', '.join(LIST_OF_CONFLICTS) + ']' if LIST_OF_CONFLICTS else ''}"
    ).replace('"', "")
    LIST_OF_CONFLICTS.append(conflict)
    character_1 = (
        format_character_name_response(
            get_response(
                prompt=f"Please generate another random but normal first name for a character.{' Please do not use any of the following: [' + ', '.join(LIST_OF_NAMES) + ']' if LIST_OF_NAMES else ''}. Name: [insert name here]"
            )
        )
        .replace('"', "")
        .replace("Name:", "")
    )
    LIST_OF_NAMES.append(character_1)
    character_2 = (
        format_character_name_response(
            get_response(
                prompt=f"Please generate another random but normal first name for a character.{' Please do not use any of the following: [' + ', '.join(LIST_OF_NAMES) + ']' if LIST_OF_NAMES else ''}. Name: [insert name here]"
            )
        )
        .replace('"', "")
        .replace("Name:", "")
    )
    LIST_OF_NAMES.append(character_2)
    personality_1 = get_response(
        prompt=f"please generate in one or two words only a personality for {character_1}."
    ).replace('"', "")
    personality_2 = get_response(
        prompt=f"please generate in one or two words only a personality for {character_2}."
    ).replace('"', "")
    characters = [
        {
            "name": f"{character_1}",
            "personality": f"{personality_1}",
            "relationship_to_target": f"{character_2} is {character_1}'s boss who is mean",
        },
        {
            "name": f"{character_2}",
            "personality": f"{personality_2}",
            "relationship_to_target": f"{character_1} is {character_2}'s employee who is tiring",
        },
    ]
    return scene, conflict, characters
