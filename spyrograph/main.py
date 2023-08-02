from random import randint,choice
from random_color import RandomColor
import turtle as t 

random_color = RandomColor()
def draw_shapes():
    """draw shapes"""
    for i in range(3,11):
        num = 360/i
        for t in range(i):
            tim.forward(100)
            tim.right(num)
            tim.color(random_color.generate_color())

t.colormode(255)
tim = t.Turtle()

# tim.shape("turtle")
tim.speed("fastest")
def another_way_to_draw():
    
    for i in range(100):
        tim.circle(100) 
        tim.right(4)
        tim.color(random_color.generate_color())


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color.generate_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        


draw_spirograph(5)




   
      

screen = t.Screen()
screen.exitonclick()