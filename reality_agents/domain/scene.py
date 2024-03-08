import random
from typing import List, Dict, Union
from utils.ascii import clear_screen, intro_text, spin

GENERIC_SIMS_STATEMENTS = [
    "Fluffing the clouds...",
    "Adjusting the ambiance...",
    "Ensuring the microphones are hidden...",
    "Infusing the air with aroma...",
    "Charging the crystals...",
    "Tidying up the place...",
    "Testing the lighting...",
    "Arranging the scenery...",
    "Adjusting the camera angles...",
    "Infusing the set with suspense...",
    "Charging the contestant's egos...",
    "Tidying up the plot twists...",
    "Polishing the on-screen chemistry...",
    "Setting the temperature...",
    "Aligning the stars...",
    "Cueing the background music...",
    "Ensuring the Wi-Fi is strong...",
    "Polishing the atmosphere...",
    "Balancing the energy levels...",
    "Harmonizing the surroundings...",
    "Refreshing the ambiance...",
    "Fine-tuning the vibes...",
    "Saturating the colors...",
    "Smoothing the edges...",
    "Summoning the spirits...",
    "Synchronizing the elements...",
    "Recharging the atmosphere...",
    "Chewing the scenery...",
]


class Scene:
    def __init__(self, scene: str):
        self.scene: str = scene.lower()
        self.initialize_scene()
        self.generate_areas()

    def initialize_scene(self) -> None:
        clear_screen()
        intro_text()
        spin(2)
        print(f"Initializing new workplace scene: {self.scene}...")
        spin(2)

    def log_sim_style(self) -> None:
        # actions: List[str] = ["Gathering", "Arranging", "Setting up", "Preparing"]
        selected_statements = random.sample(GENERIC_SIMS_STATEMENTS, 3)
        print(selected_statements[0])
        spin(1)
        print(selected_statements[1])
        spin(1)
        print(selected_statements[2])
        spin(1)

    def llm_service_simulation(
        self, scene: str
    ) -> Union[
        Dict[
            str, List[Dict[str, Union[str, List[Dict[str, Union[bool, List[bool]]]]]]]
        ],
        str,
    ]:
        simulated_response: Dict[
            str, List[Dict[str, Union[str, List[Dict[str, Union[bool, List[bool]]]]]]]
        ] = {
            "boutique": [
                {
                    "area": "Showroom",
                    "objects": [
                        {"name": "Dress Rack", "occupied": False},
                        {"name": "Checkout Counter", "occupied": [False, False]},
                    ],
                },
                # Add other areas for the boutique scene
            ],
            "auto shop": [
                {
                    "area": "Garage Bay",
                    "objects": [
                        {"name": "Car Lift", "occupied": False},
                        {"name": "Tool Chest", "occupied": False},
                    ],
                },
                # Add other areas for the auto shop scene
            ],
            # Add other scenes with similar structure
        }

        return simulated_response.get(scene, "Scene not recognized")

    def generate_areas(
        self,
    ) -> Union[
        str, List[Dict[str, Union[str, List[Dict[str, Union[bool, List[bool]]]]]]]
    ]:
        self.log_sim_style()

    def display_areas(self) -> None:
        if isinstance(self.areas, str):
            print(self.areas)
        else:
            for area in self.areas:
                print(f"Area: {area['Area']}")
                for obj in area["Objects"]:
                    occupied_status = "Yes" if obj["occupied"] else "No"
                    self.log_sim_style()
                print()
