premise = "Billy and Mark work in an auto shop. Billy is the 70-year-old owner of the shop and Mark is his 40-year-old son. They are discussing how to commit insurance fraud without actually calling it that."


def format_persona(character):
    return f"I want you to act as {character['name']}, a person who is {character['personality']}. I want you to respond using the tone, manner, and vocabulary they would use."


def format_convo_context(character, convo_state, prev_statement, target):
    # TODO for start, do
    if convo_state == "start":
        context = (
            premise
            + f" You are starting a conversation with {target['name']} who is {target['personality']}. What would you say?"
        )
    elif convo_state == "ongoing":
        context = f"How would you respond to {prev_statement} from {target['name']}?"
    else:
        context = ""

    return (
        context
        + f""" Please keep the dialogue in the style of a screenplay. Only include {character['name']}'s next line,
          so just one line of dialogue. Keep it messy and unscripted sounding, like they are half-listening to each other.
            Overall tone is the style of a trashy 2000s reality TV show."""
    )


def format_prompt(convo_state, character, prev_statement=None, target=None):
    return (
        format_persona(character)
        + " "
        + format_convo_context(character, convo_state, prev_statement, target)
    )


def format_emotion_init_prompt(persona, premise, relationship_to_target):
    return f"""Given persona: {persona}, in situation: {premise}, talking to someone who: {relationship_to_target},
      how would you initialize values for the following emotional states from 1-5: happiness, sadness, anxiety, anger, fear, boredom"""
