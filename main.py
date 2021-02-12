from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('My paddle game')
screen.tracer(0)

paddle_1 = Paddle(1)
paddle_2 = Paddle(2)

scoreboard_1 = ScoreBoard(1)
scoreboard_2 = ScoreBoard(2)

screen.listen()
screen.onkey(Paddle.up, 'Up')
screen.onkey(Paddle.down, 'Down')
# screen.onkey(paddle.left, 'Left')
# screen.onkey(paddle.right, 'Right')
scoreboard_1.write(f'Score: {scoreboard_1.score}', align='center', font=('Arial', 16, 'normal'))
scoreboard_2.write(f'Score: {scoreboard_2.score}', align='center', font=('Arial', 16, 'normal'))
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # scoreboard_1.write(f'Hello scoreboard_1.score', align='center', font=('Arial', 12, 'normal'))
    # scoreboard_2.write(f'Hello, scoreboard_1.score', align='center', font=('Arial', 12, 'normal'))
    # if screen.onkey(paddle_1.up, 'Up'):
    #     paddle_1.head.forward(Paddle.MOVE_DISTANCE)




screen.exitonclick()
