from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
scoreboard = ScoreBoard()
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
screen.update()


screen.onkeypress(key="Up",fun=right_paddle.paddle_up)
screen.onkeypress(key="Down",fun=right_paddle.paddle_down)
screen.onkeypress(key="w",fun=left_paddle.paddle_up)
screen.onkeypress(key="s",fun=left_paddle.paddle_down)

game_active = True
while(game_active):
    time.sleep(0.07)
    ball.move_ball()
    if(ball.ycor() > 270 or ball.ycor() < -270):
        print("HIT WALL")
        ball.bounce_border()

    # left_hit = (ball.distance(left_paddle) < 50 or ball.xcor() < -340)
    # right_hit = (ball.distance(right_paddle) < 50 or ball.xcor() > 340)

    if(ball.distance(right_paddle) < 50 and  ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        print("HIT PADDLE")
        ball.bounce_paddle()
    if(ball.xcor() > 350):
        print("RIGHT PADDLE MISSED")
        scoreboard.gain_point("left")
        ball.ball_reset()
        
    if(ball.xcor() < -350):
        print("LEFT PADDLE MISSED")
        scoreboard.gain_point("right")
        ball.ball_reset()
    
    screen.update()

 












screen.exitonclick()