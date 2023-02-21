from player import Player
import random as r
class Ai(Player):
    def __init__(self) -> None:
        self.name_list = ['M3gan', 'Bastion', 'BB8', 'R2D2', 'Data']
        super().__init__(r.choice(self.name_list))

    def select_gesture(self):
        self.selected_gesture = r.choice(self.gestures)
        return self.selected_gesture