import time

class GameState:
    def __init__(self):
        self.is_running = False
        self.progress = 0

    def start(self):
        self.is_running = True
        self.progress = 0
        print("Game started!")
        self.update()

    def update(self):
        while self.progress < 100:
            time.sleep(0.5)  # Simulate work
            self.progress += 10
            cli_service.update_progress_bar(self.progress)
            if self.progress >= 100:
                self.end()
                break

    def end(self):
        self.is_running = False
        self.progress = 100
        print("Game ended!")

