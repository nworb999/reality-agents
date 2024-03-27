import requests
import json
from utils.string import remove_artifacts

# TODO put this in utils, not in service layer


def get_response(prompt, past_responses=None):
    url = "http://localhost:12345/api/chat"
    if past_responses is None:
        history = []
    else:
        history = [
            {"role": "assistant", "content": message} for message in past_responses
        ]
    history.append({"role": "user", "content": remove_artifacts(prompt)})

    data = {
        # "model": "mixtral:latest",
        "model": "llama2:70b",
        # "model": "dolphin-mixtral",
        "messages": history,
        "stream": False,
    }
    print()
    print("request")
    print(data["messages"][0]["content"])
    print()
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        print("response:")
        print(response.json()["message"]["content"])
        print()
        return response.json()["message"]["content"]
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
