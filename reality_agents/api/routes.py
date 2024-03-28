from fastapi import APIRouter
from reality_agents.api.controller import GameController
from reality_agents.api.types import GameRequest

router = APIRouter()

game_controller = None


@router.post("/create-game")
def create_game(request: GameRequest):
    game_controller = GameController(
        characters=request.characters,
        conflict=request.conflict,
        scene=request.scene,
        test_flag=request.test_flag,
    )
    return game_controller.create_game()


@router.post("/start-game")
def start_game():
    return game_controller.start_game()


@router.post("/update")
def update():
    return game_controller.update()
