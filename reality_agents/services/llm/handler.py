from reality_agents.services.llm.openai import get_response as openai_response
from reality_agents.services.llm.ollama import get_response as ollama_response

model = "ollama"

response_handlers = {"openai": openai_response, "ollama": ollama_response}


# Function to get response using the specified handler
def get_response(prompt, past_responses=None):
    handler = response_handlers.get(model)
    if handler:
        return handler(prompt, past_responses)
    else:
        raise ValueError("Handler not found")
