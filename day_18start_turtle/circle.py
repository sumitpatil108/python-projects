from turtle import Turtle, Screen
import turtle
import random
t1 = Turtle()
turtle.colormode(255)

t1.pensize(5)
# dir_list = [0, 90, 180, 270]
# color = ["blue", "green", "magenta", "dark olive green", "black", "dark sea green", "cornflower blue", "beige"]
t1.speed("fastest")
def make_circle(angle):
    for _ in range(int(360 /angle) ):
        t1.color(((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
        t1.circle(100)
        t1.setheading(t1.heading() + angle)
make_circle(10)








my_screen = Screen()
my_screen.exitonclick()