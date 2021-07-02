from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        x = self.xcor()+self.x
        y = self.ycor()+self.y
        self.goto(x,y)

    def change_angle(self):
        self.y*=-1
    def change_angle_x(self):
        self.x*=-1

    def reset_position(self):
        self.goto(0,0)
        self.x*=-1
        




