from .player import Player
import time
class Human(Player):
    #initialize class with name being sent to parent
    def __init__(self, name) -> None:
        super().__init__(name)

    #Override from Player class / has person select an option and returns it
    def select_gesture(self):
        self.gesture.display_gestures()
        return self.verify_user_input()

    #verifying user input w/ either gesture name or number. If incorrect: will loop through again.
    def verify_user_input(self):
        while True:
            time.sleep(.5)
            user_input = input('\nWhich option would you like to select: ')
            for gesture in range(len(self.gesture.possible_gestures)):
                if user_input.lower() == str(gesture + 1) or user_input.lower() == self.gesture.possible_gestures[gesture]:
                    return gesture
            print('That was not a valid input! You may enter the word or number from the above options.')