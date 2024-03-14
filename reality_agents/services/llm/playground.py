from reality_agents.services.llm.ollama_handler import get_response
from reality_agents.services.llm.prompt_injection import format_prompt
from utils.ssh_tunnel import start_tunnel, stop_tunnel

if __name__ == "__main__":
    start_tunnel(
        remote_server="imagination.mat.ucsb.edu",
        ssh_username="emma",
        ssh_pkey="~/.ssh/id_rsa",
        remote_port=11434,
        local_port=12345,
    )
    print()
    # start_prompt = format_prompt(convo_state="start", character={"name":"John", "personality": "Gruff but interested"},
    #                               prev_statement="Hello", target={"name":"Mary", "personality": "Shy and not interested"})
    start_prompt = "You are 'Billy' and you own an auto shop, where your son 'Mark' works.  You are talking to Mark about a tough fix on a customer's classic car.  Insert only one statement here ____."
    print(start_prompt)
    print()
    response = get_response(start_prompt)
    print("Response", response)
    print()
    stop_tunnel()
