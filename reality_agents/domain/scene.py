import random
from typing import List, Dict, Union
from utils.ascii import clear_screen, intro_text, spin


class Scene:
    def __init__(self, scene: str):
        self.scene: str = scene.lower()
        self.initialize_scene()
        self.areas: Union[
            str, List[Dict[str, Union[str, List[Dict[str, Union[bool, List[bool]]]]]]]
        ] = self.generate_areas()

    def initialize_scene(self) -> None:
        clear_screen()
        intro_text()
        spin(2)
        print(f"Initializing new workplace scene: {self.scene}...")
        spin(2)

    def log_sim_style(self, message: str) -> None:
        actions: List[str] = ["Gathering", "Arranging", "Setting up", "Preparing"]
        print(f"{random.choice(actions)} {message}...")
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
        response = self.llm_service_simulation(self.scene)
        if isinstance(response, str):
            return response
        else:
            areas = []
            for area in response:
                self.log_sim_style(f"{area['area']} area with interactive objects")
                spin(1)
                areas.append({"Area": area["area"], "Objects": area["objects"]})
            return areas

    def display_areas(self) -> None:
        if isinstance(self.areas, str):
            print(self.areas)
        else:
            for area in self.areas:
                print(f"Area: {area['Area']}")
                for obj in area["Objects"]:
                    occupied_status = "Yes" if obj["occupied"] else "No"
                    self.log_sim_style(f"{obj['name']} (Occupied: {occupied_status})")
                print()
