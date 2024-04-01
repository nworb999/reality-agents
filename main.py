import os
import signal
import uvicorn
import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from reality_agents.api.routes import router
from utils.middleware import signal_handler, parse_arguments, RequestLoggingMiddleware
from utils.setup import setup_main_ascii, game_loop
from utils.ssh_tunnel import start_tunnel

load_dotenv()

imagination_ip = os.environ.get("IMAGINATION_IP")
imagination_port = int(os.environ.get("IMAGINATION_PORT"))
local_port = int(os.environ.get("LOCAL_PORT"))
ssh_user = os.environ.get("SSH_USERNAME")
ssh_keyfile = os.environ.get("SSH_KEYFILE")

allowed_origins = [
    "http://localhost:8000",
    "https://your-frontend-domain.com",
]

app = FastAPI(debug=True)

app.add_middleware(RequestLoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/game")


def main():
    args = parse_arguments()
    test_flag = args.test
    production_flag = args.production
    if production_flag:
        test_flag = True

    setup_main_ascii(test_flag)

    start_tunnel(
        remote_server=imagination_ip,
        ssh_username=ssh_user,
        ssh_pkey=ssh_keyfile,
        remote_port=imagination_port,
        local_port=local_port,
        test_flag=test_flag,
    )

    if not production_flag:
        game_loop(test_flag)

    if production_flag:
        uvicorn.run(app, host="0.0.0.0", port=4321)  # Start the FastAPI server
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        print("Production mode: Tunnel is open. Press Ctrl+C to stop.")
        signal.pause()  # This will block until a signal is received


if __name__ == "__main__":
    main()
