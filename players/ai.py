from .player import Player
import random as r
class Ai(Player):
    #initializing with name being randomly chosen
    def __init__(self) -> None:
        self.name_list = ['M3gan', 'Bastion', 'BB8', 'R2D2', 'Data']
        super().__init__(r.choice(self.name_list))

    #Override from Player class / Ai randomly selects an option and returns it
    def select_gesture(self):
        return r.randrange(5)