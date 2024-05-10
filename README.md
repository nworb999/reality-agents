# reality agents

## setup
If you're connecting to a local LLM with ollama, you may also need to run `ollama serve` in the imagination server (or wherever ollama is hosted) to launch the instance. 
 ```bash
 python3 -m venv reality-env
 source reality-env/bin/activate
 pip install -r requirements.txt
 python main.py --test
```

This currently expects an SSH tunnel to a remote server that has ollama running.  In the future, I can add a flag to turn that off.  The environment variables go as follows:

```
IMAGINATION_IP=
IMAGINATION_PORT=11434 # ollama port
LOCAL_PORT= # arbitrary
SSH_USERNAME=
SSH_KEYFILE=
```


## architecture

Read more [here](./reality_agents/README.md)


## reflections

I would have added frontend functionality, asynchronous programming and websockets from the get-go.  I would have grouped prompts more from the beginning based on the associated step.  I also would have started using Pydantic types sooner.  I also shouldn't have dismissed the benefits of using a tool like Langchain but I'm happy to have had the experience to write a lot of stuff myself.

Also I'm not using Poetry again, I forgot about good old venv in my time away from Python.
