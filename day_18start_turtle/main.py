from turtle import Turtle, Screen
import random
t1 = Turtle()
# t2 = Turtle()
# t2.setx(10)
# t2.sety(10)
t1.shape("turtle")
color = ["blue", "green", "magenta", "dark olive green"]
#square
t1.color(random.choice(color))
for _ in range(4):
       t1.forward(180)
       t1.right(90)
#t1.left(90)
#triangle
t1.color(random.choice(color))
for _ in range(3):
    t1.forward(180)
    t1.right(120)
#pentagon
t1.color(random.choice(color))
for _ in range(5):
    t1.forward(180)
    t1.right(72)
#hexagon
t1.color(random.choice(color))
for _ in range(6):
    t1.forward(180)
    t1.right(60)

# for i in range(10):
#     t2.forward(15)
#     t2.penup()
#     t2.forward(5)
#     t2.pendown()
my_screen = Screen()
my_screen.exitonclick()
