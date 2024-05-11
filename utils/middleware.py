import sys
import json
import argparse
from fastapi import Request
from reality_agents.api.types import GameRequest
from starlette.middleware.base import BaseHTTPMiddleware
from utils.ssh_tunnel import stop_tunnel

models = ["openai", "ollama"]


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body = await request.body()
        # print(GameRequest.model_json_schema())
        # try:
        #     body_json = json.loads(body)
        #     print("Request body:", body_json)
        # except json.JSONDecodeError:
        #     print("Request body is not JSON")
        response = await call_next(request)
        return response


def signal_handler(signum, frame):
    print("Shutting down...")
    stop_tunnel()
    sys.exit(0)


def parse_arguments():
    parser = argparse.ArgumentParser(description="A reality TV script generator.")
    parser.add_argument("--test", action="store_true", help="Run quickly in test mode")
    parser.add_argument(
        "--production",
        action="store_true",
        help="Run in production mode with the SSH tunnel open",
    )
    parser.add_argument(
        "--model", type=str, choices=models, help="The language model provider to use."
    )
    parser.add_argument(
        "--no-tunnel",
        action="store_true",
        help="Don't open an SSH tunnel to the remote server",
    )
    return parser.parse_args()
