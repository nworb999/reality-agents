def format_persona(personality):
    str = f"Given that your personality is {personality},"
    return str


def format_convo_context(convo_state, prev_statement, target, target_personality):
    if convo_state == "start":
        str = f"and you are starting a conversation with {target} who is {target_personality}, what would you say?"
    if convo_state == "ongoing":
        str = f"how would you respond to {prev_statement} from {target}?"
    return str + "Please keep the dialogue to one line that is extremely informal."


def format_prompt(
    convo_state,
    personality,
    prev_statement=None,
    target=None,
    target_personality=None,
):
    prompt = format_persona(personality) + format_convo_context(
        convo_state, prev_statement, target, target_personality
    )
    return prompt
