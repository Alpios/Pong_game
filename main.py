from ball import Ball
from turtle import  Turtle,Screen
from board_movement import Board
from scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.listen()

screen.tracer(0)
board_r = Board((350,0))
board_l = Board((-350,0))
ball=Ball()
scoreboard = Scoreboard()

screen.onkey(board_r.move_up, "Up")
screen.onkey(board_r.move_down, "Down")
screen.onkey(board_l.move_up, "w")
screen.onkey(board_l.move_down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.ball_speed)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #collision with right paddle
    if ball.distance(board_r)<50 and ball.xcor()>320 or ball.distance(board_l)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #Detect when paddle misses the ball
    if ball.xcor()>420:
        ball.ball_reset_position()
        ball.bounce_x()
        scoreboard.score_increase_left()
    #Detect when left paddle misses the ball
    if ball.xcor()<-420:
        ball.ball_reset_position()
        ball.bounce_x()
        scoreboard.score_increase_right()



screen.exitonclick()