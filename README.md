# reality agents 👺

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
[Try our beta now!](https://nworb999.github.io/reality-agents-ui/)

<img width="1011" alt="chart" src="https://github.com/nworb999/reality-agents/assets/20407156/81ac27ac-3f53-483f-843a-1415c8d9fda6">


## setup
If you're connecting to a local LLM with ollama, you may also need to run `ollama serve` in the imagination server (or wherever ollama is hosted) to launch the instance. 
 ```bash
 python3 -m venv reality-env
 source reality-env/bin/activate
 pip install -r requirements.txt
 python main.py --test
```

If you're running on a server where ollama is running, make the LOCAL_PORT in the `.env` 11434 and leave the imagination (remote) server variables blank.  Then run `python main.py --test --no-tunnel`.

```
IMAGINATION_IP=
IMAGINATION_PORT=11434 # ollama port
LOCAL_PORT= # arbitrary unless ollama port when running the program in a server where ollama is running.
SSH_USERNAME=
SSH_KEYFILE=
```

If you're running on a cuttlefish, run this:

```
python main.py --cuttlefish --no-tunnel --model openai
```


## architecture

Read more [here](./reality_agents/README.md)


## reflections

I would have added frontend functionality, asynchronous programming and websockets from the get-go.  I would have grouped prompts more from the beginning based on the associated step.  I also would have started using Pydantic types sooner.  I also shouldn't have dismissed the benefits of using a tool like Langchain but I'm happy to have had the experience to write a lot of stuff myself.

Also I'm not using Poetry again, I forgot about good old venv in my time away from Python.
