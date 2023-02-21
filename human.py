from player import Player
import time
class Human(Player):
    def __init__(self) -> None:
        super().__init__()

    def select_gesture(self):
        self.display_gestures()
        self.verify_user_input()
        return self.selected_gesture

    def display_gestures(self):
        print('\nPlease make your selection:\n')
        for gesture in range(len(self.gestures)):
            time.sleep(.5)
            print(f'{gesture + 1} - {self.gestures[gesture]}')
        print()

    def verify_user_input(self):
        while True:
            time.sleep(.5)
            user_input = input('Which option would you like to select: ')
            for gesture in range(len(self.gestures)):
                if user_input.lower() == str(gesture) or user_input.lower() == self.gestures[gesture]:
                    self.selected_gesture = self.gestures[gesture]
                    return None
            print('That was not a valid input! You may enter the word or number from the above options.')