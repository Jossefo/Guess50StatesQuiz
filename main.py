import turtle
import pandas
#####################################################################
"""Function : every time you click - Prints the [x,y] cordinates """
# def get_mouse_click_cor (x,y):
#     print(x,y)
#####################################################################

screen = turtle.Screen()
screen.title("U.S 50 States Quiz")
image_of_us = "blank_states_img.gif"
turtle.addshape(image_of_us)
turtle.shape(image_of_us)

#####################################################################
"""this is to get the x,y cordinates of each state on the US Map """
# turtle.onscreenclick(get_mouse_click_cor)
#
# turtle.mainloop()
#####################################################################
states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
states_answered = []
while len(states_answered) < 50 :
    answer = screen.textinput(title=f"{len(states_answered)}/50 correct states " ,
                              prompt="Enter a US State: ").title()
    if answer == "Exit":
        break
    if answer in states_list:
        states_answered.append(answer)
        screen_text_turtle = turtle.Turtle()
        screen_text_turtle.ht()
        screen_text_turtle.penup()
        curr_state_data = states_data[states_data.state == answer]
        screen_text_turtle.goto(int(curr_state_data.x) , int(curr_state_data.y))
        screen_text_turtle.write((curr_state_data.state.item()))

missing_states = [state for state in states_list if state not in states_answered]
missing_states_data = pandas.DataFrame(missing_states)
missing_states_data.to_csv("states_to_learn.csv")

screen.exitonclick()