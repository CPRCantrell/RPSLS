from os import system, name
from gestures.gestures import *
class Player:
    #initialize gestures and other attributes needed for score tracking
    def __init__(self, name) -> None:
        self.name = name
        self.points = 0
        self.round_winner:bool = False
        self.gesture = Gestures()

    #Overriden by Child classes
    def select_gesture(self):
        pass

    #Sets 2 players against eachother
    def battle(p1, p2):
        p1.round_winner = False
        p2.round_winner = False
        Player._clear_screen()
        print(f'{p1.name} is going\n')
        p1.gesture = p1.gesture.set_gesture(p1.select_gesture())
        Player._clear_screen()
        print(f'{p2.name} is going\n')
        p2.gesture = p2.gesture.set_gesture(p2.select_gesture())
        Player._clear_screen()
        p1.round_winner = p1.gesture.win_fight(p2.gesture)
        p2.round_winner = p2.gesture.win_fight(p1.gesture)

    #Override string to print gesture selected
    def __str__(self) -> str:
        return self.name.title()

    #clears the terminal
    def _clear_screen() -> None:
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')