import os
import argparse
from dotenv import load_dotenv
from utils.setup import setup_main_ascii, game_loop
from utils.ssh_tunnel import start_tunnel, stop_tunnel

load_dotenv()

imagination_ip = os.environ.get("IMAGINATION_IP")
imagination_port = int(os.environ.get("IMAGINATION_PORT"))
local_port = int(os.environ.get("LOCAL_PORT"))
ssh_user = os.environ.get("SSH_USERNAME")
ssh_keyfile = os.environ.get("SSH_KEYFILE")


def parse_arguments():
    parser = argparse.ArgumentParser(description="A reality TV script generator.")
    parser.add_argument("--test", action="store_true", help="Run quickly in test mode")
    return parser.parse_args()


def main():
    args = parse_arguments()
    test_flag = args.test
    setup_main_ascii(test_flag)
    start_tunnel(
        remote_server=imagination_ip,
        ssh_username=ssh_user,
        ssh_pkey=ssh_keyfile,
        remote_port=imagination_port,
        local_port=local_port,
        test_flag=test_flag,
    )
    game_loop(test_flag)
    stop_tunnel()


if __name__ == "__main__":
    main()
