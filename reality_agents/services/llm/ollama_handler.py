import requests
import json


def get_response(prompt, past_responses=None):
    url = "http://localhost:12345/api/chat"
    if past_responses is None:
        history = []
    else:
        history = [{"role": "user", "content": message} for message in past_responses]
    history.append({"role": "user", "content": prompt})
    print("the history", history)
    data = {
        "model": "mixtral:latest",
        # "model": "llama2:70b",
        "messages": history[:5],
        "stream": False,
    }
    # print()
    # print(data)
    # print()
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json()["message"]["content"]
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
