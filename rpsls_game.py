from os import system, name
from human import Human
from ai import Ai
class RpslsGame:
    def __init__(self) -> None:
        self._player_list = []

    def display_welcome(self) -> None:
        RpslsGame._clear_screen()
        print("Welcome to the Rock, Paper, Scissors, Lizzard, Spock Game")

    def perform_round(self) -> None:
        pass

    def determine_winner(self, player_one, gesture_one, player_two, gesture_two):
        pass

    def display_overall_winner(self) -> None:
        pass

    def display_rules(self) -> None:
        print("\n\nYou will choose the either play by yourself against an AI, or against another player")
        print("When the game starts, you will be given an opportunity to select which gesture you")
        print("want to throw. You will pick from the following list of gestures:")
        print("\nRock\nPaper\nScissors\nLizzard\nSpock")
        print("\nFor whichever gesture you choose, it will be able to beat 2 other gestures and will")
        print("be able to be beaten by two other gestures.")
        input("\n\n\n\nPress ENTER to choose the players")

    def play(self) -> None:
        while self._player_list[0].points < 2 and self._player_list[1].points < 2:
            self.perform_round()

    def assign_players(self) -> None:
        selection_made = False
        self._player_list.append(Human("Player 1"))
        RpslsGame._clear_screen()
        print("Please choose the player settings:\n\n")
        print("1. You versus an AI Player")
        print("2. You versus another human Player\n")
        while not selection_made:
            try:
                input_string = input("\nYour Selection: ")
                input_as_int = int(input_string)
                if input_as_int == 1:
                    self._player_list.append(Ai("AI Player"))
                    print("\nCreated Human versus AI game")
                    selection_made = True
                elif input_as_int == 2:
                    self._player_list.append(Human("Player 2"))
                    print("\nCreated Human versus AI game")
                    selection_made = True
                else:
                    raise Exception()
            except:
                print("Input not recognized")
        input("Press enter when you are ready to play")

    def _clear_screen() -> None:
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


