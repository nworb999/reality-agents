from utils.logger import logger
import asyncio
from fastapi import APIRouter, WebSocket, status
from starlette.websockets import WebSocketDisconnect
from fastapi.responses import JSONResponse
from reality_agents.api.controller import GameController
from reality_agents.api.types import GameRequest
from utils.logger import print_capture_handler


router = APIRouter()
game_controller = None


@router.post("/create")
def create_game(request: GameRequest):
    global game_controller
    try:
        print_capture_handler.clear_logs()

        game_controller = GameController(
            characters=request.characters,
            conflict=request.conflict,
            scene=request.scene,
            test_flag=True,
            max_turns=request.max_turns if request.max_turns else 10,
        )

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Game created successfully",
            },
        )
    except ConnectionError as ce:
        logger.error(f"Connection error: {ce}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "message": "Connection error, please try again later",
            },
        )
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise


@router.post("/start")
def start_game():
    try:
        if game_controller is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"message": "Game not created"},
            )
        game_controller.start_game()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Game started successfully",
            },
        )
    except ConnectionError as ce:
        logger.error(f"Connection error: {ce}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "message": "Connection error, please try again later",
            },
        )
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise


@router.post("/update")
def update():
    try:
        if game_controller is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"message": "Game not started"},
            )
        game_controller.update()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Game updated successfully",
            },
        )
    except ConnectionError as ce:
        logger.error(f"Connection error: {ce}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"message": "Connection error, please try again later"},
        )
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise


@router.get("/logs")
def get_logs():
    try:
        if game_controller is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"message": "Game not started or no logs available"},
            )
        # Assume print_capture_handler is accessible and holds the latest logs
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Logs fetched successfully",
                "logs": print_capture_handler.logs,
            },
        )
    except Exception as e:
        logger.error(f"Error fetching logs: {e}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal server error"},
        )
