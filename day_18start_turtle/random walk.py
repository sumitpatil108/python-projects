from turtle import Turtle, Screen
import turtle
import random
t1 = Turtle()
turtle.colormode(255)

t1.pensize(15)
dir_list = [0, 90, 180, 270]
color = ["blue", "green", "magenta", "dark olive green", "black", "dark sea green", "cornflower blue", "beige"]

i=0
while i<200:
    #t1.color(random.choice(color))
    t1.color(((random.randint(0,255),random.randint(0,255),random.randint(0,255))))
    t1.forward(25)
    t1.setheading(random.choice(dir_list))
    i+=1








my_screen = Screen()
my_screen.exitonclick()