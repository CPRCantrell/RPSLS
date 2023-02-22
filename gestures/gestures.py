import time
class Gestures:
    def __init__(self,gesture=None, weak_to=None) -> None:
        self.gesture = gesture
        self.weak_to = weak_to
        self.possible_gestures = ['rock','paper','scissors','lizard','spoke']

    #Checks if the gesture wins the fight
    def win_fight(self, opponent):
        for weakness in opponent.weak_to:
            if self.gesture == weakness:
                return True
        return False

    #Displays gesture options
    def display_gestures(self):
        for gesture in range(len(self.possible_gestures)):
            time.sleep(.5)
            print(f'{gesture + 1} - {self.possible_gestures[gesture]}')

    #set class gesture
    def set_gesture(self,postion):
        class_gestures = [Rock(),Paper(),Scissors(),Lizard(),Spock()]
        return class_gestures[postion]

    #override string to print name
    def __str__(self) -> str:
        return self.gesture.title()

class Rock(Gestures):
    def __init__(self) -> None:
        super().__init__('rock',['spock','paper'],)

class Paper(Gestures):
    def __init__(self) -> None:
        super().__init__('paper',['lizard','scissors'])

class Scissors(Gestures):
    def __init__(self) -> None:
        super().__init__('scissors',['spock','rock'])

class Lizard(Gestures):
    def __init__(self) -> None:
        super().__init__('lizard',['rock','scissors'])

class Spock(Gestures):
    def __init__(self) -> None:
        super().__init__('spock',['lizard','paper'])