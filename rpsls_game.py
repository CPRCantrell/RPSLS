from os import system, name

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
        print("Rock\nPaper\nScissors\nLizzard\nSpock")
        print("\nFor whichever gesture you choose, it will be able to beat 2 other gestures and will")
        print("be able to be beaten by two other gestures.")
        input("\n\n\n\nPress ENTER to choose the players")
    def play(self) -> None:
        pass

    def assign_players(self) -> None:
        pass

    def _clear_screen() -> None:
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')