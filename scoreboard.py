from turtle import Turtle


class ScoreBoard(Turtle):
    ALIGNMENT = 'center'
    FONT = ('Arial', 16, 'normal')
    STARTING_POSITION_1 = (-50, 270)
    STARTING_POSITION_2 = (50, 270)

    def __init__(self, starting_position):
        super().__init__()
        self.starting_position = starting_position
        self.color('white')
        self.penup()
        self.hideturtle()
        self.create_scoreboard()
        self.score = 0

    def create_scoreboard(self):
        if self.starting_position == 1:
            self.goto(ScoreBoard.STARTING_POSITION_1)
        elif self.starting_position == 2:
            self.goto(ScoreBoard.STARTING_POSITION_2)

    def update_scoreboard(self):
        pass
