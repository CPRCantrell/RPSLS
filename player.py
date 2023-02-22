class Player:
    #initialize gestures and other attributes needed for score tracking
    def __init__(self, name) -> None:
        self.name = name
        self.points = 0
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.selected_gesture = None

    #Overridden in child classes (Human & Ai)
    def select_gesture():
        pass

    #Override string to print gesture selected
    def __str__(self) -> str:
        self.selected_gesture