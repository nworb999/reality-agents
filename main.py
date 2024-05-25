import os
import signal
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from reality_agents.api.routes import router
from utils.middleware import signal_handler, parse_arguments, RequestLoggingMiddleware
from utils.setup import setup_main_ascii, game_loop
from utils.ssh_tunnel import start_tunnel
import reality_agents.services.llm.handler as handler
from utils.constants import (
    IMAGINATION_IP,
    IMAGINATION_PORT,
    LOCAL_PORT,
    SSH_USERNAME,
    SSH_KEYFILE,
)


allowed_origins = [
    "http://localhost:8080",
    "https://nworb999.github.io/reality-agents-ui/",
    f"http://{IMAGINATION_IP}:{IMAGINATION_PORT}",
    f"http://localhost:{LOCAL_PORT}",
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

model = "ollama"


def main():
    args = parse_arguments()
    if args.model:
        handler.model = args.model
    test_flag = args.test
    production_flag = args.production
    if production_flag:
        test_flag = True

    setup_main_ascii(test_flag)

    tunnel_flag = args.no_tunnel
    if not tunnel_flag:
        start_tunnel(
            remote_server=IMAGINATION_IP,
            ssh_username=SSH_USERNAME,
            ssh_pkey=SSH_KEYFILE,
            remote_port=IMAGINATION_PORT,
            local_port=LOCAL_PORT,
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
