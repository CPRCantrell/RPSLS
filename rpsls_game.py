from os import system, name
from human import Human
from ai import Ai
class RpslsGame:
    def __init__(self) -> None:
        self._player_list = []

    def display_welcome(self) -> None:
        RpslsGame._clear_screen()
        print("Welcome to the Rock, Paper, Scissors, Lizzard, Spock Game")
        print("---------------------------------------------------------")

    def perform_round(self) -> None:
        RpslsGame._clear_screen()
        print("Current scores: ")
        print(f"{self._player_list[0].name}: {self._player_list[0].points}")
        print(f"{self._player_list[1].name}: {self._player_list[1].points}\n\n")
        print(f"Currently playing: {self._player_list[0].name}")
        self._player_list[0].select_gesture()

        if type(self._player_list[1]) == Human:
            RpslsGame._clear_screen()
            input("Press ENTER when you have switched players")
            RpslsGame._clear_screen()
            print(f"Currently playing: {self._player_list[1].name}")
            self._player_list[1].select_gesture()
            input("Press ENTER to see the winner")
        else:
            self._player_list[1].select_gesture()
        RpslsGame._clear_screen()
        print(f"{self._player_list[0].name} threw {self._player_list[0]}")
        print(f"{self._player_list[1].name} threw {self._player_list[1]}\n\n")
        winner_list = self.determine_winner()
        if len(winner_list) == 2:
            print("It's a tie!")
        else:
            print(f"{winner_list[0].name} wins!")
            winner_list[0].points += 1
        input("\n\n\nPress ENTER for the next round")

    def __display_gesture_choices(player):
        for i in range(0, player.gestures):
            print(f"{i + 1}. {player.gestures[i]}")

    def __get_valid_gesture_selection(self) -> int:
        valid_selection = False
        selection_index = -1
        print("\n\n")
        while not valid_selection:
            input_as_string = input("Your Selection: ")
            try:
                selection_index = int(input_as_string)
                selection_index -= 1
                if selection_index < 0 or selection_index > (len(self._player_list[0].gestures) - 1):
                    raise Exception()
                else:
                    valid_selection = True
            except:
                print("Invalid selection\n")
        return selection_index

    #determines winner of each round
    def determine_winner(self):
        gesture_win_against = {'rock':['lizard', 'scissors'], 'paper':['rock', 'spock'], 'scissors':['lizard', 'paper'], 'lizard':['spock','paper'], 'spock':['rock', 'scissors']}
        for lossing_gesture in gesture_win_against[self._player_list[0].selected_gesture]:
            if self._player_list[1].selected_gesture == lossing_gesture:
                return [self._player_list[0]]
        for lossing_gesture in gesture_win_against[self._player_list[1].selected_gesture]:
            if self._player_list[0].selected_gesture == lossing_gesture:
                return [self._player_list[1]]
        return self._player_list

    #determines and displays overall winner
    def display_overall_winner(self) -> None:
        self._clear_screen()
        print(f'\n\nThe winner is {self._player_list[0].name if self._player_list[0].points == 2 else self._player_list[1].name}!\n\n')

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
                    self._player_list.append(Ai())
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


game = RpslsGame()

game.display_welcome()
game.display_rules()
game.assign_players()
game.play()