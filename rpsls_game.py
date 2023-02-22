from os import system, name
import time
from human import Human
from ai import Ai
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
        self.__perform_player_half(self._player_list[0])
        self.__perform_player_half(self._player_list[1])
        self.__display_round_results()

    #Displays the results of the round
    def __display_round_results(self) -> None:
        RpslsGame._clear_screen()
        print(f"{self._player_list[0].name} threw {self._player_list[0]}")
        print(f"{self._player_list[1].name} threw {self._player_list[1]}\n\n")
        winner_list = self.determine_winner()
        if len(winner_list) == 2:
            print("It's a tie!")
        else:
            print(f"{winner_list[0].name} wins!")
            winner_list[0].points += 1
        print("\n\n")
        self.__display_scores()
        if self._player_list[0].points != 2 and self._player_list[1].point != 2:
            input("\n\nPress ENTER for the next round")
        else:
            input("\n\nPress ENTER to see the winner!")

    #Displays the current scores
    def __display_scores(self) -> None:
        print("Current scores")
        print("--------------")
        print(f"{self._player_list[0].name}: {self._player_list[0].points}")
        print(f"{self._player_list[1].name}: {self._player_list[1].points}\n\n")

    #Performs a selection screen if the Player is human, just selects in the Player is an AI
    def __perform_player_half(self, player) -> None:
        if type(player) == Human:
            RpslsGame._clear_screen()
            self.__display_scores()
            print(f"Currently playing: {player.name}")
            player.select_gesture()
            RpslsGame._clear_screen()
            if player is self._player_list[0] and type(self._player_list[1]) == Human:
                input("Press ENTER when to move to the next player")
            else:
                input("Press ENTER when ready to see the results")
        else:
            player.select_gesture()

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
        print("2. You versus another human Player\n")
        print("3. AI versus AI")
        while not selection_made:
            try:
                input_string = input("\nYour Selection: ")
                input_as_int = int(input_string)
                if input_as_int == 1:
                    self._player_list.append(Human("You"))
                    self._player_list.append(Ai())
                    print("\nCreated Human versus AI game")
                    selection_made = True
                elif input_as_int == 2:
                    self._player_list.append(Human("You"))
                    self._player_list.append(Human("Player 2"))
                    print("\nCreated Human versus AI game")
                    selection_made = True
                elif input_as_int == 3:
                    self._player_list.append(Ai())
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
        input("Press enter when you are ready to play")

    #clears the terminal
    def _clear_screen() -> None:
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')