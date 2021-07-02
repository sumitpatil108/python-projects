from turtle import Turtle
# HIGHSCORE = 0
# high_score = open("game.txt","w")
# high_score.write(str(HIGHSCORE))
# high_score = open("game.txt","r")
# HIGHSCORE = high_score.read()
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        with open("game.txt", "r") as file:
            self.highscore = int(file.read())

        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.write(f"Score {self.score} High score { self.highscore }", align="center", font=("Arial", 24, "normal"))
    def game_over(self):
        if self.score > self.highscore:

            with open("game.txt", "w") as file:
                file.write(str(self.score))

        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))


    def detect_colission_score(self):
        self.score+=1
        self.clear()
        self.update_score()




