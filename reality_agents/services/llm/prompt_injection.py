situation = """Billy and Mark work in an auto shop. Billy is the 70-year-old owner of the shop and
 Mark is his 40-year-old son.  They are discussing a tough fix on a customer's classic car.
     """

template = " Insert only one statement here ____."


def format_persona(character):
    return f"""I want you to act as {character['name']}, a person who is {character['personality']}.
      I want you to respond using the tone, manner, and vocabulary they would use."""


def format_convo_context(character, convo_state, prev_statement, target):
    if convo_state == "start":
        context = (
            situation
            + f" You are {character['name']} starting a conversation with {target['name']} who is {target['personality']}."
            + template
        )
    elif convo_state == "ongoing":
        context = (
            f"How would you respond to the last statement from {target['name']}?"
            + template
        )
    else:
        context = ""

    return context + f"""Overall tone is the style of a trashy 2010s reality TV show."""


def format_prompt(convo_state, character, prev_statement=None, target=None):
    return (
        format_persona(character)
        + " "
        + format_convo_context(character, convo_state, prev_statement, target)
    )


def format_emotion_init_prompt(persona, situation, relationship_to_target):
    return f"""Given persona: {persona}, in situation: {situation}, talking to someone who: {relationship_to_target},
      how would you initialize values for the following emotional states from 1-5: happiness, sadness, anxiety, anger, fear, boredom"""
