import os
import sys
import signal
import argparse
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from reality_agents.api.routes import router
from utils.setup import setup_main_ascii, game_loop
from utils.ssh_tunnel import start_tunnel, stop_tunnel

load_dotenv()

imagination_ip = os.environ.get("IMAGINATION_IP")
imagination_port = int(os.environ.get("IMAGINATION_PORT"))
local_port = int(os.environ.get("LOCAL_PORT"))
ssh_user = os.environ.get("SSH_USERNAME")
ssh_keyfile = os.environ.get("SSH_KEYFILE")


app = FastAPI()  # Create a FastAPI app
app.include_router(router)  # Include the router


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
    return parser.parse_args()


def main():
    args = parse_arguments()
    test_flag = args.test
    production_flag = args.production

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
