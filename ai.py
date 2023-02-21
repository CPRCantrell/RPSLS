from player import Player
import random as r
class Ai(Player):
    def __init__(self) -> None:
        super().__init__()

    def select_gesture(self):
        self.selected_gesture = r.choice(self.gestures)
        return self.selected_gesture