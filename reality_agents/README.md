# architecture

Originally this app was designed to support multiple talking agents, but it was challenge enough to have a believable dialogue between two, so the focus narrowed to just two conversing agents.

## domain layer
This layer will handle game logic, game state, entities/models, and game types.

## api layer
This layer will define RESTful endpoints such as starting a game, getting the current state of the game, and updating the game state. It will also handle how data is received from and sent to the client, including parsing requests and formatting responses. It also handles validation of data coming in through the API.  

It controls the logic of the game at a very high level.

## service layer
This layer processes requests from the API layer, applying business rules that are not directly part of the core game logic. This includes determining which game type a request refers to. It will also act as a mediator between the API layer and the domain layer, calling upon the domain layer to carry out game-related operations. The domain layer and the API layer should remain separate, otherwise. The service layer will also handle interactions with the database.

The services layer creates the different entities within a game and combines them into the game logic class.

## view layer
This layer makes API calls to control the game at a high level while translating it to visual output.