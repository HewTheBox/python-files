from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(5,5)
        self.color("red")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
        
    def ball_movement(self):
        # self.setx(-730)
        # self.sety(330)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.speed("fastest")
    def ball_bounce(self):
        self.y_move*=-1
        
    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9
        
        
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        