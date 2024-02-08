import requests
import json


def get_response(prompt, history=[]):
    print(prompt)
    url = "http://localhost:12345/api/chat"
    if history is not None:
        history.append({"role": "user", "content": prompt})
    else:
        history = [{"role": "user", "content": prompt}]

    data = {
        "model": "llama2:70b",
        "messages": history,
        "stream": False,
    }

    data_json = json.dumps(data)

    headers = {"Content-Type": "application/json"}
    print(data)
    response = requests.post(url, data=data_json, headers=headers)
    print(response)
    print(response.text)
    return

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
