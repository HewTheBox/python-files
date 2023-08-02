from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
game_is_on = True
screen.listen()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    

    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    
    if snake.all_turtles[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
        
    #Detct collision with wall.
    head = snake.all_turtles[0]

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        game_is_on = False
        score.game_o0ver()
        
    # Detect collision with tail
    for segment in snake.all_turtles[1:]:
        
        if snake.all_turtles[0].distance(segment) < 10:
            game_is_on - False
            score.game_o0ver()

















screen.exitonclick()