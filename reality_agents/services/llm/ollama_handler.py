import requests
import json


def get_response(prompt, history=[]):
    # print()
    # print(prompt)
    # print()
    url = "http://localhost:12345/api/chat"
    if history is not None:
        history.append({"role": "user", "content": prompt})
    else:
        history = [{"role": "user", "content": prompt}]

    data = {
        # "model": "llama2:70b",
        "model": "mixtral:latest",
        "messages": history,
        "stream": False,
    }

    data_json = json.dumps(data)

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=data_json, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
    return response_data["message"]["content"]


# with history
note = """ 
     "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    },
    {
      "role": "assistant",
      "content": "due to rayleigh scattering."
    },
    {
      "role": "user",
      "content": "how is that different than mie scattering?"
    }
    ]
    """
