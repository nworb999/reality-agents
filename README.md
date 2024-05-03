# reality agents

## setup
If you're connecting to a local LLM with ollama, you may also need to run `ollama serve` in the imagination server (or wherever ollama is hosted) to launch the instance. 

 ```bash
 source reality-env/bin/activate
 python main.py --test
```


## architecture

Read more [here](./reality_agents/README.md)


## reflections

I would have added frontend functionality, asynchronous programming and websockets from the get-go.  I would have grouped prompts more from the beginning based on the associated step.  I also would have started using Pydantic types sooner.  