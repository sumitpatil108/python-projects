from turtle import Turtle
import random
COLOR = ["red","green","blue","purple","yellow","orange"]
I = 5

class Racer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color("black")
        self.setheading(180)
        # self.INCREAMENT = 15
        self.I = 5

    def genrate(self):
        self.penup()

        position_y = random.randint(-250,250)
        # position_x = random.randint(280,380)
        self.goto(300,position_y)
        self.color(COLOR[random.randint(0,5)])

    def go(self):

        self.forward(I)








