from os import system, name
from players.human import Human
from players.ai import Ai
import time
class RpslsGame:
    def __init__(self) -> None:
        self._player_list = []

        self.display_welcome()
        self.display_rules()
        self.assign_players()
        self.play()
        self.display_overall_winner()

    #Displays welcome message
    def display_welcome(self) -> None:
        RpslsGame._clear_screen()
        print("Welcome to the Rock, Paper, Scissors, Lizzard, Spock Game")
        print("---------------------------------------------------------")

    #Plays a single round
    def perform_round(self) -> None:
        Human.battle(self._player_list[0], self._player_list[1])
        self.__display_round_results()

    #Displays the results of the round
    def __display_round_results(self) -> None:
        RpslsGame._clear_screen()
        print(f"{self._player_list[0]} threw {self._player_list[0].gesture}")
        print(f"{self._player_list[1]} threw {self._player_list[1].gesture}\n\n")

        if self._player_list[0].round_winner:
            self._player_list[0].points += 1
            print(f"{self._player_list[0]} won!")
        elif self._player_list[1].round_winner:
            self._player_list[1].points += 1
            print(f"{self._player_list[1]} won!")
        else:
            print("It's a tie!")

        print("\n\n")
        self.__display_scores()
        if self._player_list[0].points != 2 and self._player_list[1].points != 2:
            input("\n\nPress ENTER for the next round")
        else:
            input("\n\nPress ENTER to see the winner!")

    #Displays the current scores
    def __display_scores(self) -> None:
        print("Current scores")
        print("--------------")
        print(f"{self._player_list[0]}: {self._player_list[0].points}")
        print(f"{self._player_list[1]}: {self._player_list[1].points}\n\n")

    #Loop rounds
    def play(self) -> None:
        while self._player_list[0].points < 2 and self._player_list[1].points < 2:
            self.perform_round()

    #Determines winner of each round
    def determine_winner(self):
        gesture_win_against = {'rock':['lizard', 'scissors'], 'paper':['rock', 'spock'], 'scissors':['lizard', 'paper'], 'lizard':['spock','paper'], 'spock':['rock', 'scissors']}
        for lossing_gesture in gesture_win_against[self._player_list[0].selected_gesture]:
            if self._player_list[1].selected_gesture == lossing_gesture:
                return [self._player_list[0]]
        for lossing_gesture in gesture_win_against[self._player_list[1].selected_gesture]:
            if self._player_list[0].selected_gesture == lossing_gesture:
                return [self._player_list[1]]
        return self._player_list

    #Determines and displays overall winner
    def display_overall_winner(self) -> None:
        RpslsGame._clear_screen()
        print(f'\n\nThe winner is {self._player_list[0].name if self._player_list[0].points == 2 else self._player_list[1].name}!\n\n')

    #displays the rules
    def display_rules(self) -> None:
        print("\n\nYou will choose to either play against an AI, or against another player")
        print("When the game starts, you will be given an opportunity to select which gesture you")
        print("want to throw. You will pick from the following list of gestures:")
        print("\nRock\nPaper\nScissors\nLizard\nSpock")
        print('\nRules are as followed:\n')
        rules_list = ['Rock crushes Scissors','Scissors cuts Paper','Paper covers Rock','Rock crushes Lizard','Lizard poisons Spock','Spock smashes Scissors','Scissors decapitates Lizard','Lizard eats Paper','Paper disproves Spock','Spock vaporizes Rock']
        for rule in rules_list:
            time.sleep(.2)
            print(f'{rule}')
        input("\n\n\n\nPress ENTER to choose the players")

    #Asks player for HvH, HvA, or AvA
    def assign_players(self) -> None:
        selection_made = False

        RpslsGame._clear_screen()
        print("Please choose the player settings:\n\n")
        print("1. You versus an AI")
        print("2. You versus another human Player")
        print("3. AI versus AI")
        while not selection_made:
            try:
                input_string = input("\n\nYour Selection: ")
                input_as_int = int(input_string)
                if input_as_int == 1:
                    self._player_list.append(Human("Player 1"))
                    self._player_list.append(Ai())
                    print("\nCreated Human versus AI game")
                    selection_made = True
                elif input_as_int == 2:
                    self._player_list.append(Human("Player 1"))
                    self._player_list.append(Human("Player 2"))
                    print("\nCreated Human versus AI game")
                    selection_made = True
                elif input_as_int == 3:
                    self._player_list.append(Ai())
                    selection_made = True
                    print("\nCreated AI vs AI game")
                    duplicate_name = True
                    while duplicate_name:
                        temp_ai = Ai()
                        if temp_ai.name != self._player_list[0].name:
                            self._player_list.append(temp_ai)
                            duplicate_name = False
                else:
                    raise Exception()
            except:
                print("Input not recognized")
        input("\n\nPress enter when you are ready to play")

    #clears the terminal
    def _clear_screen() -> None:
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')