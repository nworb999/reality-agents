from typing import Optional

template = "Provide one sentence."

# TODO refactor as args objects
# TODO separate into separate files -- prompt templates


def format_convo_summary_prompt(
    current_memory,
    objective,
    conflict,
    personality,
    emotional_state,
    utterance,
    relationship_to_target,
):
    prefix = (
        f"Briefly update the following conversation summary: {current_memory}"
        if current_memory
        else "Generate a brief summary of a conversation"
    )
    prompt = f""" from the perspective of 
    someone who is {personality} in emotional state: {emotional_state} talking to someone who is
    {relationship_to_target}.  The conflict is: {conflict}, and the objective is {objective}.  The other person has just said: {utterance}."""
    return prefix + prompt


def format_persona(character, target, conflict, scene):
    return f"""Roleplay as {character.name} (who is {character.personality}) talking to {target.name} (relationship: {character.relationship_to_target}) about {conflict} in the workplace: {scene}."""


def format_convo_context(character, convo_state, target, utterance):
    if convo_state == "start":
        context = f"You are starting a conversation.  What do you say?"
    elif convo_state == "ongoing":
        context = f"""Conversation so far:  {character.get_memory() if character.get_memory() else 'None'}
            
            Given that {target.name} just said {utterance}, how do you respond?."""
    else:
        context = ""

    return (
        context
        + f" Your current intention is: [{character.get_intention()}]."
        + template
    )


def format_prompt(convo_state, character, conflict, scene, target, utterance):
    return (
        format_persona(
            character=character, target=target, conflict=conflict, scene=scene
        )
        + " "
        + format_convo_context(
            character=character,
            convo_state=convo_state,
            target=target,
            utterance=utterance,
        )
    )


def format_emotion_init_prompt(
    persona, conflict, relationship_to_target, utterance=None
):
    return f"""
        Given a persona: {persona}, who is in a conflict: {conflict}, and is talking to someone who: {relationship_to_target}{f'-- they just said: {utterance}.' if utterance else ''}
    what would be a realistic emotional state for the character?  Please return a single bullet point incorporating multiple emotions.

    * [insert emotional state]
    """


def format_emotion_update_prompt(utterance, state):
    return f"""Given the following utterance: {utterance}, how would you update the emotional state of the character: {state}?
        Please return a single bullet point incorporating multiple emotions.
        
    * [insert emotional state]
    """


def format_objective_init_prompt(
    persona, conflict, scene, relationship_to_target, emotional_state, utterance=None
):
    return f"""You are roleplaying as a character with persona: {persona}, who is in a conflict about: {conflict} taking place in scene: {scene}, talking to someone with the following relationship: {relationship_to_target}. Your emotional state is: {emotional_state},
     {f'The other person has just said: {utterance}.' if utterance else ''}.  What would a sensible objective for the conversation be?  It should be self-serving and incoherent.  Make a list of tactics for the conversation with the following format, followed by a summary of the objective in one bullet.

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


def format_init_intention_prompt(
    objective, persona, tactics, emotional_state, utterance=None
):
    return f"""You are roleplaying as a character with persona: {persona} and emotional state: {emotional_state} -- you are in a conversation where you are trying to achieve objective: {objective}. {f'The other person has just said: {utterance}.' if utterance else ''}
    Your tactics include {tactics}.  Pick one tactic to use for the first intention of the character.  Please only return a bullet point.
    
    Intention: [insert intention]"""


def format_update_intention_prompt(memory, emotional_state, current_tactic, utterance):
    return f"""Conversation so far: {memory}, emotional state: {emotional_state}, previous tactic: {current_tactic},
    and the following utterance: {utterance} --
    what be a sensible intention for the character? Please return only one bullet point.
    
    Intention: [insert intention]"""


def format_rerun_objective_init_prompt(objective, raw_tactics):
    return f"""Given the objective: {objective} and the raw tactics: {raw_tactics}, please make a numbered tactical plan for 
    the conversation that would accomplish that objective in clear steps.  List tactics for a range of psychological states.

    Tactical plan: 

    1. [first step]
    2. [second step]
    3. [third step] (...and so on)
    """


def format_intention_to_end_conversation_prompt(persona, utterance, objective):
    return f"""Persona: {persona}, previous statement: {utterance}.  You are trying
     to end the conversation, what would you say next?"""


def format_did_conversation_end_prompt(utterances):
    return f"""Given the last few lines of dialogue, is the game over? {utterances}.  Yes or no?"""


# leave on cliffhanger
