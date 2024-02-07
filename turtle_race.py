from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 650, height = 650)
user_bet = screen.textinput(title = "Make your bet", prompt = "WHO WILL WIN (choose color)?")
all_turtles = []
colors = ["red", "blue", "green", "yellow", "purple", "black"]
y_positions = [300, 200, 100, -100, -200, -300]
x_position = 300

def start_position(turtle_list):
    
    for turtle in turtle_list:
        y_pos = y_positions[turtle_list.index(turtle)]
        turtle.penup()
        turtle.goto(x = -x_position, y = y_pos)
        turtle.pendown()
def moving(turtle_list):
    is_end = False
    end_of_canvas = screen.window_width()/2

    while not is_end:
        for turtle in turtle_list:
            move_distance = random.randint(1,20)
            turtle.forward(move_distance)
            if turtle.xcor() < end_of_canvas:
                continue
            else:
                is_end = True
                if user_bet == turtle.color():
                    print(f"Race is finished. YOU WON THE BET {turtle.color()} is the winner")
            print(f"{turtle.color()[0].upper()} turtle has won the race. YOU LOSE")

for num in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[num])
    all_turtles.append(new_turtle)
    
start_position(all_turtles)
moving(all_turtles)

screen.exitonclick()













