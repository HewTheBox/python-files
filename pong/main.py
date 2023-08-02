from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)
screen.listen()



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
scoreboard = Scoreboard()


screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()

game_is_on = True



while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_movement()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce()
        
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        
        ball.bounce_x()
        
        
    #Detect r misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    #Detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        

screen.exitonclick()