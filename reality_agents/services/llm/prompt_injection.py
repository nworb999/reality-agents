template = "Use the previous dialogue and respond accordingly.  Provide one sentence."


def format_persona(character):
    return f"""Speak exactly like {character.name}, a person who is {character.personality} with {character.pronouns} pronouns. Avoid reusing any of the adjectives from the personality."""


def format_convo_context(character, convo_state, conflict, scene, target):
    if convo_state == "start":
        context = f" You are {character.name} starting a conversation with {target.name} who is {target.personality} and uses {target.pronouns} pronouns.  You are currently having conflict: {conflict} in {scene}"
    elif convo_state == "ongoing":
        context = f"How would you respond to the last statement from {target.name}?"
    else:
        context = ""

    return (
        context
        + f" The character's current intention is {character.get_intention()}, so accomplish that with the next utterance.  "
        + template
    )


def format_prompt(convo_state, character, conflict, scene, target=None):
    return (
        format_persona(character)
        + " "
        + format_convo_context(character, convo_state, conflict, scene, target)
    )


def format_emotion_init_prompt(persona, conflict, relationship_to_target):
    return f"""Given persona: {persona}, in conflict: {conflict}, talking to someone who: {relationship_to_target},
      how would you initialize values for the following emotional states from 1-5: happiness, sadness, anxiety, anger, fear, boredom.
          Please only return them in a Python dictionary."""


def format_emotion_update_prompt(utterance, states):
    return f"""Given the following utterance: {utterance}, how would you update these emotional states of the character: {states}?
        Please only return them in a Python dictionary."""


def format_objective_init_prompt(
    persona, conflict, relationship_to_target, emotional_state
):
    return f"""Given persona: {persona}, in conflict: {conflict}, talking to someone who: {relationship_to_target}, and emotional state: {emotional_state},
    what would a sensible objective for the conversation be?  Please only return a one sentence objective."""


# relies on history of conversation, or feed in utterance
def format_should_update_objective_prompt(
    objective, persona, conflict, emotional_state, convo_history=None
):
    return f"""Given Persona: {persona}, Conflict: {conflict}, Emotional state: {emotional_state}, Dialogue :{convo_history} --
     would it make sense to deviate from the current conversation objective: {objective}?  Yes or no?.  Note: only change the objective if absolutely necessary."""


# relies on history of conversation, or feed in utterance
def format_update_objective_prompt(
    old_objective, conflict, persona, emotional_state, convo_history=None
):
    return f"""What would a sensible new objective for the conversation be considering the old objective: {old_objective}, the conflict: {conflict}, the agent's personality: {persona}, and their current emotional state: {emotional_state}?  Please only return a one sentence objective."""


def format_is_objective_fulfilled_prompt(
    objective, persona, conflict, emotional_state, convo_history=None
):
    # if yes, intention to end conversation is set
    return f"""Given Persona: {persona}, Conflict: {conflict}, Emotional State: {emotional_state}, discussion: {convo_history} --
     has the current conversation objective: {objective} been fulfilled?  Yes or no?."""


def format_init_intention_prompt(objective, persona, conflict, emotional_state):
    return f"""Given Persona: {persona}, Conflict: {conflict}, Objective: {objective} and emotional state: {emotional_state} -- 
    what would be a sensible intention for the next response of a character?  Please only return a one sentence intention."""


def format_update_intention_prompt(emotional_state, objective, utterance):
    return f"""Emotional state: {emotional_state}, Objective: {objective}, and the following utterance: {utterance} --
    what be a sensible intention for the character?  Based on what was said, so how can they move the convesation forward?  Should they ask for further clarification or suggest a strategy?  Please only return a one sentence intention."""


def format_intention_to_end_conversation_prompt(persona, utterance, objective):
    return f"""Persona: {persona}, Previous utterance: {utterance}.  You are trying
     to end the conversation, what would you say next?"""


def format_did_conversation_end_prompt(utterances):
    return f"""Given the last few lines of dialogue, is the game over? {utterances}.  Yes or no?"""


# leave on cliffhanger
