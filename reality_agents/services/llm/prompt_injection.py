template = " Insert only one brief statement here ____."


def format_persona(character):
    return f"""Speak exactly like {character.name}, a person who is {character.personality} with {character.pronouns} pronouns.
        Keep responses brief, natural, and informal.  Avoid goofy colloquialisms or reusing any of the adjectives from the personality."""


def format_convo_context(character, convo_state, situation, target):
    if convo_state == "start":
        context = (
            situation
            + f" You are {character.name} starting a conversation with {target.name} who is {target.personality}."
            + template
        )
    elif convo_state == "ongoing":
        context = (
            f"How would you respond to the last statement from {target.name}?"
            + template
        )
    else:
        context = ""

    return (
        context
        + f" The character's current emotional state is {character.emotional_state.__str__}.  "
    )


def format_prompt(convo_state, character, situation, target=None):
    return (
        format_persona(character)
        + " "
        + format_convo_context(character, convo_state, situation, target)
    )


def format_emotion_init_prompt(persona, situation, relationship_to_target):
    return f"""Given persona: {persona}, in situation: {situation}, talking to someone who: {relationship_to_target},
      how would you initialize values for the following emotional states from 1-5: happiness, sadness, anxiety, anger, fear, boredom.
          Please only return them in a Python dictionary, no justification or explanation necessary."""


def format_emotion_update_prompt(utterance, states):
    return f"""Given the following utterance: {utterance}, how would you update these emotional states of the character: {states}?
        Please only return them in a Python dictionary, no justification or explanation necessary."""
