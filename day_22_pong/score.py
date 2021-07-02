from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.write(f"{self.l_score}", align="center", font=("Arial", 24, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Arial", 24, "normal"))
    def update(self):
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Arial", 24, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Arial", 24, "normal"))

    def score_l(self):
        self.l_score+=1
        self.clear()
        self.update()

    def score_r(self):
        self.r_score+=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))


