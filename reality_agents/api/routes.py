from utils.logger import print_capture_handler, logger
import asyncio
from fastapi import APIRouter, WebSocket, status
from fastapi.responses import JSONResponse
from reality_agents.api.controller import GameController
from reality_agents.api.types import GameRequest


router = APIRouter()

game_controller = None


@router.post("/create")
def create_game(request: GameRequest):
    global game_controller

    game_controller = GameController(
        characters=request.characters,
        conflict=request.conflict,
        scene=request.scene,
        test_flag=True,
    )

    game_controller.create_game()
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Game created successfully"},
    )


@router.post("/start")
def start_game():
    if game_controller is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Game not created"},
        )
    game_controller.start_game()
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "Game started successfully"}
    )


@router.post("/update")
def update():
    if game_controller is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Game not started"},
        )
    game_controller.update()
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "Game updated successfully"}
    )


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(1)  # Adjust the frequency of messages as needed
        if print_capture_handler.latest_message:
            await websocket.send_text(print_capture_handler.latest_message)
            print_capture_handler.latest_message = ""
