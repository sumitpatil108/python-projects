from turtle import Turtle, Screen

tim = Turtle()
def frw():
    tim.forward(50)
def bkr():
    tim.backward(50)
def angle_l():
    new_heading = tim.heading() +10
    tim.setheading(new_heading)
def angle_r():
    new_heading = tim.heading() -10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.onkey(frw, "Up")
screen.onkey(bkr, "w")
screen.onkey(angle_l,"a")
screen.onkey(angle_r, "r")
screen.listen()
screen.exitonclick()