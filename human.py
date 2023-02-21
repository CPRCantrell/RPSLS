from player import Player
import sys
class Human(Player):
    def __init__(self) -> None:
        super().__init__()

    def select_gesture(self):
        self.display_gestures()
        self.verify_user_input()

    def diplay_gestures(self):
        print('Please make your selection:\n')
        for gesture in range(len(self.gestures)):
            print(f'{gesture + 1} - {self.gestures[gesture]}')
        print()

    def verify_user_input(self):
        while True:
            user_input = input('Which option would you like to select: ')
            for gesture in range(len(self.gestures)):
                if user_input.lower() == str(gesture) or user_input.lower() == self.gestures[gesture]:
                    self.selected_gesture = self.gestures[gesture]
                    return
            self.__clear__()
            print('That was not a valid input! You may enter the word or number from the above options.')

    def __clear__(lines=1):
        for line in range(lines):
            sys.stdout.write('\033[F')
            sys.stdout.write('\033[K')
