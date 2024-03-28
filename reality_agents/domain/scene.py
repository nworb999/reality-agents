import random
from typing import List, Dict, Union
from utils.ascii import clear_screen, intro_text, spin
from utils.constants import GENERIC_SIMS_STATEMENTS


def initialize_scene(scene, test_flag=False):
    # get spin out of domain
    if not test_flag:
        clear_screen()
        intro_text()
        spin(2)
        print(f"Initializing new workplace scene: {scene}...")
        spin(2)


def generate_areas(test_flag=False):
    if not test_flag:
        log_sim_style(test_flag)


def display_areas(areas):
    if isinstance(areas, str):
        print(areas)
    else:
        for area in areas:
            print(f"Area: {area['Area']}")
            for obj in area["Objects"]:
                occupied_status = "Yes" if obj["occupied"] else "No"
                log_sim_style()
            print()


def log_sim_style():
    # actions: List[str] = ["Gathering", "Arranging", "Setting up", "Preparing"]
    selected_statements = random.sample(GENERIC_SIMS_STATEMENTS, 3)
    for statement in selected_statements:
        print(statement)
        spin(2)


def llm_service_simulation(scene: str):
    simulated_response = {
        "boutique": [
            {
                "area": "Showroom",
                "objects": [
                    {"name": "Dress Rack", "occupied": False},
                    {"name": "Checkout Counter", "occupied": [False, False]},
                ],
            },
        ],
        "auto shop": [
            {
                "area": "Garage Bay",
                "objects": [
                    {"name": "Car Lift", "occupied": False},
                    {"name": "Tool Chest", "occupied": False},
                ],
            },
        ],
        # Add other scenes with similar structure
    }

    return simulated_response.get(scene, "Scene not recognized")


class Scene:
    def __init__(self, scene: str):
        self.scene: str = scene.lower()
