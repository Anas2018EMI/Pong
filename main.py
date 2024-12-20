from turtle import Screen
from paddles import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

ball= Ball()

scoreboard= Scoreboard()

paddle_right=Paddle((350,0))
paddle_left=Paddle((-350,0))

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "z")
screen.onkey(paddle_left.move_down, "s")

start_game=True
while start_game:
    screen.update()
    time.sleep(0.05 )
    ball.move()
    # Detect collision with the paddles
    if (ball.distance(paddle_right) < 50 and ball.xcor()> 330) or (ball.distance(paddle_left) < 50 and ball.xcor()< -330):
        ball.setheading(-180-ball.heading())
        ball.forward_pace +=2
    
    # Check scores and reposition the ball
    new_scorer=ball.check_missed_balls()
    if new_scorer=='right':
        scoreboard.right_paddle_scores()
    elif new_scorer=='left':
        scoreboard.left_paddle_scores()
        












screen.exitonclick()