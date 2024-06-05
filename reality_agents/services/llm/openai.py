import openai
import os
from utils.string import remove_artifacts
from dotenv import load_dotenv
import time

# TODO put this in utils, not in service layer

load_dotenv()

client = openai.OpenAI(api_key=os.environ.get("OPENAI_KEY"))


def get_response(prompt, past_responses=None):
    time.sleep(4)
    if past_responses is None:
        past_responses = []

    messages = [{"role": "user", "content": message} for message in past_responses]
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-4o-2024-05-13",  # Ensure you specify the correct model, e.g., gpt-3.5-turbo if needed
        messages=messages,
    )

    return response.choices[0].message.content
