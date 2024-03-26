template = "Use the previous dialogue and disagree accordingly.  Provide one sentence."


def format_persona(character):
    return f"""Roleplay as {character.name}, a person who is {character.personality}."""


def format_convo_context(character, convo_state, conflict, scene, target):
    if convo_state == "start":
        context = f"You are starting a conversation with {target.name} (relationship?: {target.relationship}).  You are currently having conflict: {conflict} in workplace: {scene}"
    elif convo_state == "ongoing":
        context = f"How would you respond to the last statement from {target.name}?  They are {target.personality}.  You are in workplace: {scene}."
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
    return f"""
        Given a persona: {persona}, who is in a conflict: {conflict}, and is talking to someone who: {relationship_to_target},
    what would be a realistic emotional state for the character?  Please only return a single bullet point incorporating some or all of the following emotions: happiness, sadness, anxiety, anger, fear, and boredom.

    * [insert emotional state]
    """


def format_emotion_update_prompt(utterance, state):
    return f"""Given the following utterance: {utterance}, how would you update the emotional state of the character: {state}?
        Please only return a single bullet point incorporating some or all of the following emotions: happiness, sadness, anxiety, anger, fear, and boredom.
        
    * [insert emotional state]
    """


def format_objective_init_prompt(
    persona, conflict, relationship_to_target, emotional_state
):
    return f"""You are roleplaying as a character with persona: {persona}, who is in a conflict about: {conflict}, talking to someone with the following relationship: {relationship_to_target}, and emotional state: {emotional_state},
    what would a sensible objective for the conversation be?  It should be selfish and contentious.  Make a list of tactics for the conversation with the following format, followed by a summary of the objective in one bullet.

Tactical plan:

1. [insert first step]
2. [insert second step]
3. [insert third step] (...and so on)

* Objective: [insert objective]"""


def format_is_objective_fulfilled_prompt(
    objective, persona, conflict, emotional_state, convo_history=None
):
    # if yes, intention to end conversation is set
    return f"""You are roleplaying as a character with persona: {persona}, Conflict: {conflict}, Emotional State: {emotional_state}, discussion: {convo_history} --
     has the current conversation objective: {objective} been fulfilled?  Yes or no?."""


def format_init_intention_prompt(objective, persona, tactics, emotional_state):
    return f"""You are roleplaying as a character with persona: {persona} and emotional state: {emotional_state} -- you are in a conversation where you are trying to achieve objective: {objective}.
    Your tactics include {tactics}.  Pick one tactic to use for the first intention of the character.  Please only return a bullet point.
    
    Intention: [insert intention]"""


def format_update_intention_prompt(emotional_state, objective, utterance):
    return f"""Emotional state: {emotional_state}, Objective: {objective}, and the following utterance: {utterance} --
    what be a sensible intention for the character?  Based on what was said, so how can they move the conversation forward?  Should they ask for further clarification or suggest a strategy?  Please only return a one sentence intention."""


def format_rerun_objective_init_prompt(objective, raw_tactics):
    return f"""Given the objective: {objective} and the raw tactics: {raw_tactics}, please make a numbered tactical plan for the conversation that would accomplish that objective in clear steps.

    Tactical plan: 

    1. [first step]
    2. [second step]
    3. [third step] (...and so on)
    """


def format_intention_to_end_conversation_prompt(persona, utterance, objective):
    return f"""Persona: {persona}, Previous utterance: {utterance}.  You are trying
     to end the conversation, what would you say next?"""


def format_did_conversation_end_prompt(utterances):
    return f"""Given the last few lines of dialogue, is the game over? {utterances}.  Yes or no?"""


# leave on cliffhanger
