# reality agents

## setup

After cloning the repository, you need to set up the project environment using Poetry. If you haven't already installed Poetry, you can find installation instructions on the [Poetry website](https://python-poetry.org/docs/).

If you're connecting to a local LLM with ollama, you also need to run `ollama serve` in the imagination server (or wherever ollama is hosted) to launch the instance. 

 ```bash
 poetry install
 poetry shell # use virtual environment
 poetry run python --version # confirm version matches the pyproject.toml
 poetry run python main.py
```

## tests

```bash
poetry run pytest
```


## architecture

Read more [here](./reality_agents/README.md)

## frameworks

In the future, I might need to convert this project into a web-based application. In that case, I would use a framework like FastAPI. 
