premise = "Billy and Mark work in an auto shop."


def format_persona(character):
    str = f"""I want you to act as {character['name']}, a person who is {character['personality']}.  I want you to respond using the tone, manner and vocabulary they
would use."""
    return str


def format_convo_context(convo_state, prev_statement, target):
    if convo_state == "start":
        str = (
            premise
            + f"You are starting a conversation with {target['name']} who is {target['personality']}.  What would you say?"
        )
    if convo_state == "ongoing":
        # need to use history -- how to keep context short?
        str = f"how would you respond to {prev_statement} from {target['name']}?"
    return str + "Please keep the dialogue to one line that is extremely informal."


def format_prompt(
    convo_state,
    character,
    prev_statement=None,
    target=None,
):
    prompt = format_persona(character) + format_convo_context(
        convo_state, prev_statement, target
    )
    return prompt
