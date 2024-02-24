import random
from utils.ascii import clear_screen, intro_text, spin


class Scene:
    def __init__(self, scene):
        self.scene = scene.lower()
        clear_screen()
        intro_text()
        spin()
        print(f"Initializing new workplace scene: {self.scene}...")
        self.areas = self.generate_areas()
        spin()

    def log_sim_style(self, message):
        actions = ["Gathering", "Arranging", "Setting up", "Preparing"]
        print(f"{random.choice(actions)} {message}...")

    def llm_service_simulation(self, scene):
        # Placeholder for the hypothetical llm service.
        self.log_sim_style(f"props and backdrops for {scene}")

        simulated_response = {
            # if a character isn't at an object it's assumed they are standing with each other
            "boutique": [
                {
                    "area": "Showroom",
                    "objects": [
                        {"name": "Dress Rack", "occupied": False},
                        {"name": "Checkout Counter", "occupied": [False, False]},
                    ],
                },
                {
                    "area": "Fitting Room",
                    "objects": [
                        {"name": "Mirror", "occupied": False},
                        {
                            "name": "Seating Area",
                            "occupied": [False, False, False, False],
                        },
                    ],
                },
                {
                    "area": "Stock Room",
                    "objects": [
                        {"name": "Inventory Shelves", "occupied": False},
                        {"name": "Restocking Cart", "occupied": False},
                    ],
                },
                {
                    "area": "Manager's Office",
                    "objects": [
                        {"name": "Desk", "occupied": False},
                        {"name": "File Cabinet", "occupied": False},
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
                {
                    "area": "Waiting Room",
                    "objects": [
                        {"name": "Seats", "occupied": [False, False, False, False]},
                        {"name": "Coffee Machine", "occupied": False},
                    ],
                },
                {
                    "area": "Office",
                    "objects": [
                        {"name": "Desk", "occupied": False},
                        {"name": "Computer", "occupied": False},
                    ],
                },
                {
                    "area": "Storage Room",
                    "objects": [
                        {"name": "Spare Parts Shelves", "occupied": False},
                        {"name": "Tire Rack", "occupied": False},
                    ],
                },
            ],
            # Add other scenes with similar structure
        }

        return simulated_response.get(scene, "Scene not recognized")

    def generate_areas(self):
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

    def display_areas(self):
        if isinstance(self.areas, str):
            print(self.areas)
        else:
            for area in self.areas:
                print(f"Area: {area['Area']}")
                for obj in area["Objects"]:
                    self.log_sim_style(
                        f"{obj['name']} (Occupied: {'Yes' if obj['occupied'] else 'No'})"
                    )
                print()
