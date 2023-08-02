from turtle import Turtle
SNAKE_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.all_turtles = []
        
        self.create_snake()
        # self.head = self.all_turtles[0]
        
    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position=position)
            
            
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_turtles.append(new_segment)
        
    def extend(self):
        self.add_segment(self.all_turtles[-1].position())
           
    def move(self): 
        
        for num in range(len(self.all_turtles)-1, 0, -1):
            new_x = self.all_turtles[num -1].xcor()
            new_y = self.all_turtles[num -1].ycor()
            self.all_turtles[num].goto(new_x, new_y)
            
        self.all_turtles[0].forward(20)
        
    def up(self):
        if self.all_turtles[0].heading() != DOWN:
            self.all_turtles[0].setheading(90)
        
    def down(self):
        if self.all_turtles[0].heading() != UP:
            self.all_turtles[0].setheading(270)
        
    def right(self):
        if self.all_turtles[0].heading() != LEFT:
            self.all_turtles[0].setheading(0)
        
    def left(self):
        if self.all_turtles[0].heading() != RIGHT:
            self.all_turtles[0].setheading(180)
        
    
        
    