import sys
import argparse
from utils.ssh_tunnel import stop_tunnel


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
