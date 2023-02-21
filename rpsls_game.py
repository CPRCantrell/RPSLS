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
        pass

    def assign_players(self) -> None:
        selection_made = False
        player1 = Human()
        player1.name = "Player 1"
        self._player_list.append(Human())
        while not selection_made:
            try:
                RpslsGame._clear_screen()
                print("Please choose the player settings:\n\n")
                print("1. You versus an AI Player")
                print("2. You versus another human Player")
                input_string = input("\n\nYour Selection: ")
                input_as_int = int(input_string)
                if input_as_int == 1:
                    player2 = Ai()
                    player2.name = "AI Player"
                    self._player_list.append(Ai())
                    selection_made = True
                elif input_as_int == 2:
                    player2 = Ai()
                    player2.name = "Player 2"
                    self._player_list.append(Human())
                    selection_made = True
                else:
                    raise Exception()
            except:
                print("Input not recognized")


    def _clear_screen() -> None:
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


game = RpslsGame()
game.display_welcome()
game.display_rules()
game.assign_players()
game.play()