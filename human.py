from player import Player

class Human(Player):
    def __init__(self) -> None:
        super().__init__()

    def select_gesture(self):
        self.display_gestures()
        user_input = self.get_input()
        return user_input