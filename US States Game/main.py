import turtle
import pandas
import time
screen = turtle.Screen()
screen.tracer(0)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()
tim.write(" ", align="center", font=("Courier", 10, "normal"))
tim.hideturtle()
tim.penup()


# code to help get all the cordinates of the states of the map

# def mouse_onlick_value(x, y):
#     print(x, y)
    
# screen.onscreenclick(mouse_onlick_value)
# turtle.mainloop()




states_name = pandas.read_csv("50_states.csv")
data = states_name.to_dict()
states_data = states_name.state
all_data = []
for i in range(0,50):
    name = data["state"][i]
    x = data["x"][i]
    y = data["y"][i]
    mytuple = (name, x, y)
    all_data.append(mytuple)
    
states = []
file = []
game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.01)
    screen.update()
    
    answer_state = screen.textinput(f"{count}/50 States Correct", "What's another states name?: ")
    if answer_state == "exit":
        for state in states_data:
            if state not in states:
                file.append(state)
        break
    correct = False
    for i in range(0, len(all_data)):
        if all_data[i][0] == answer_state.title():
            x = all_data[i][1]
            y = all_data[i][2]
            tim.goto(x=x, y=y)
            tim.write(f"{all_data[i][0]}", align="center", font=("Courier", 10, "normal"))
            correct = True
            states.append(all_data[i][0])
            
            
    if not correct:
        tim.goto(x=0, y=0)
        tim.write(f"Game Over\nScore: {count}", align="center", font=("Courier", 20, "normal"))
        game_is_on = False
        
    count+=1


to_convert = pandas.DataFrame(file)
to_convert.to_csv("missed_states.csv")



# screen.exitonclick()