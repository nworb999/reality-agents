template = "Keep the dialogue a bit boring. Insert only one brief statement here ____."


def format_persona(character):
    return f"""Speak exactly like {character.name}, a person who is {character.personality} with {character.pronouns} pronouns.
        Keep responses brief, natural, and informal.  Avoid reusing any of the adjectives from the personality."""


def format_convo_context(character, convo_state, conflict, target):
    if convo_state == "start":
        context = (
            conflict
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


def format_prompt(convo_state, character, conflict, target=None):
    return (
        format_persona(character)
        + " "
        + format_convo_context(character, convo_state, conflict, target)
    )


def format_emotion_init_prompt(persona, conflict, relationship_to_target):
    return f"""Given persona: {persona}, in conflict: {conflict}, talking to someone who: {relationship_to_target},
      how would you initialize values for the following emotional states from 1-5: happiness, sadness, anxiety, anger, fear, boredom.
          Please only return them in a Python dictionary, followed by a one sentence justification."""


def format_emotion_update_prompt(utterance, states):
    return f"""Given the following utterance: {utterance}, how would you update these emotional states of the character: {states}?
        Please only return them in a Python dictionary, followed by a one sentence justification."""


def format_objective_init_prompt(
    persona, conflict, relationship_to_target, emotional_state
):
    return f"""Given persona: {persona}, in conflict: {conflict}, talking to someone who: {relationship_to_target}, and emotional state: {emotional_state},
    what would a sensible objective for the conversation be?  Please only return a one sentence objective."""


# relies on history of conversation, or feed in utterance
def format_should_update_objective_prompt(
    objective, persona, conflict, emotional_state
):
    return f"""Given persona: {persona}, in conflicts: {conflict}, and emotional state: {emotional_state}, 
     would it make sense to change the current conversation objective: {objective}?  Yes or no?."""


# relies on history of conversation, or feed in utterance
def format_update_objective_prompt():
    return f"""What would a sensible new objective for the conversation be?  Please only return a one sentence objective."""


def format_is_objective_fulfilled_prompt(objective, persona, conflict, emotional_state):
    # if yes, intention to end conversation is set
    return f"""Given persona: {persona}, in conflict: {conflict}, and emotional state: {emotional_state}, 
     has the current conversation objective: {objective} been fulfilled?  Yes or no?."""


def format_init_intention_prompt(objective, persona, conflict, emotional_state):
    return f"""Given persona: {persona}, in conflict: {conflict}, with objective: {objective} and emotional state: {emotional_state}, 
    what would be a sensible intention for the next response of a character?  Please only return a one sentence intention."""


def format_update_intention_prompt(emotional_state, utterance):
    return f"""Given the emotional state: {emotional_state}, and the following utterance: {utterance}, 
    what be a sensible intention for the character?  Please only return a one sentence intention."""


def format_intention_to_end_conversation(persona, utterance, objective):
    return f"""Given persona: {persona}, the previous utterance: {utterance}, the fact that objective: {objective} feels accomplished, and the fact that you are trying
     to end the conversation, what would you say next?"""


# leave on cliffhanger
