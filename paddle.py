from turtle import Turtle


class Paddle:
    STARTING_POSITION_1 = [(-380, 0), (-380, -20), (-380, -40)]
    STARTING_POSITION_2 = [(380, 0), (380, -20), (380, -40)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270

    def __init__(self, starting_position: int):
        """Начальная позиция для игрока 1 и 2 вносится при инициализации
        экземпляра класса"""
        self.segments = []
        self.starting_position = starting_position
        self.create_paddle()
        self.head = self.segments[0]

    def create_paddle(self):
        if self.starting_position == 1:
            for position in Paddle.STARTING_POSITION_1:
                self.add_segment(position)
        elif self.starting_position == 2:
            for position in Paddle.STARTING_POSITION_2:
                self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

    def up(self):
        self.head.setheading(Paddle.UP)

    def down(self):
        self.head.setheading(Paddle.DOWN)
