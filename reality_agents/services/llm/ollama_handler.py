import requests
import json


def get_response(prompt, history=None):
    # print()
    # print(prompt)
    # print()
    url = "http://localhost:12345/api/chat"
    if history is None:
        history = []

    history.append({"role": "user", "content": prompt})

    data = {
        "model": "mixtral:latest",
        "messages": history,
        "stream": False,
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json()["message"]["content"]
    else:
        print(f"Request failed with status code {response.status_code}")
        return None


# Example usage
note = """
    "messages": [
        {
            "role": "user",
            "content": "why is the sky blue?"
        },
        {
            "role": "assistant",
            "content": "due to Rayleigh scattering."
        },
        {
            "role": "user",
            "content": "how is that different than Mie scattering?"
        }
    ]
"""
