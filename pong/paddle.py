from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(position)
        self.color("white")
        self.penup()
        
        
    def up(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)
    def down(self):
        newY =    self.ycor() - 20
        self.goto(self.xcor(), newY)