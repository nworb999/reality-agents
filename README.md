# reality agents

## setup
If you're connecting to a local LLM with ollama, you may also need to run `ollama serve` in the imagination server (or wherever ollama is hosted) to launch the instance. 

 ```bash
 python3 -m venv reality-env
 pip install -r requirements.txt
 source reality-env/bin/activate
 python main.py --test
```


## architecture

Read more [here](./reality_agents/README.md)


## reflections

I would have added frontend functionality, asynchronous programming and websockets from the get-go.  I would have grouped prompts more from the beginning based on the associated step.  I also would have started using Pydantic types sooner.  I also shouldn't have dismissed the benefits of using a tool like Langchain but I'm happy to have had the experience to write a lot of stuff myself.

Also I'm not using Poetry again, I forgot about good old venv in my time away from Python.
