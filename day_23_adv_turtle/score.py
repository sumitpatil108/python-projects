from turtle import Turtle

FONT = ("Courier",24,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-258,258)
        self.show()

    def show(self):
        self.clear()
        self.write(f"level : { self.level}",align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def increment(self):
        self.level+=1
        self.show()

