import turtle
from turtle import *
import pandas as pd


def write_text(x, y, state):

    tim = Turtle()
    tim.penup()
    tim.hideturtle()
    tim.goto(x, y)
    tim.write(f"{state}", move=False)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(width=735, height=505)
screen.addshape(image) # this to add the shape in the screen cuz we can't use a shape if it's not in the screen
turtle.shape(image)



# read the csv file
states = pd.read_csv("50_states.csv")


score = 0
all_states = states['state'].to_list()
guessed_states=[]

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    correct_answer = states[states['state'] == answer_state]
    if answer_state =="Exit":
        rest_states = set(all_states) - set(guessed_states)
        missed_states = list(rest_states)
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv('states_to_learn.csv')

        break

    if not correct_answer.empty:
        guessed_states.append(answer_state)
        xcor = correct_answer['x'].values
        ycor = correct_answer['y'].values
        state_name = correct_answer['state'].values
        write_text(xcor[0], ycor[0], state_name[0])
        score+=1


screen.mainloop()



