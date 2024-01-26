# reality agents

## setup

After cloning the repository, you need to set up the project environment using Poetry. If you haven't already installed Poetry, you can find installation instructions on the [Poetry website](https://python-poetry.org/docs/).

 ```bash
   poetry install
   poetry shell # use virtual environment
   poetry run python --version # confirm version matches the pyproject.toml
```

## tests

```bash
    poetry run pytest
```


## architecture

### domain layer

This layer will handle game logic, game state, entities/models, and game types.

### api layer

This layer will define RESTful endpoints such as starting a game, getting the current state of the game, and updating the game state.  It will also handle how data is received from and sent to the client, including parsing requests and formatting responses.  It also handles validation of data coming in through the API.

### service layer

This layer processes requests from the API layer, applying business rules that are not directly part of the core game logic.  This includes determining which game type a request refers to.  It will also act as a mediator between the API layer and the domain layer, calling upon the domain layer to carry out game-related operations.  The domain layer and the API layer should remain separate, otherwise.  The service layer will also handle interactions with the database.

## frameworks

In the future, I might need to convert this project into a web-based application. In that case, I would use a framework like FastAPI. 