from turtle import Turtle
from day_23_adv_turtle.racer import Racer

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("red")
        self.goto(0,-280)

    def forward1(self):
        self.forward(10)

    def finish_line(self):
       if self.ycor()>280:

           return True
       else:
           return False

    def start(self):
        self.goto(0,-280)




