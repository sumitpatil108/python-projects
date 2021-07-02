from turtle import Turtle, Screen
from day_23_adv_turtle.racer import Racer
import day_23_adv_turtle.racer
from day_23_adv_turtle.player import Player
from day_23_adv_turtle.score import Score
import time
import random

my_screen = Screen()
my_screen.setup(width=600,height=600)
list_box = []

my_screen.tracer(0)
my_screen.listen()

player = Player()
score = Score()
my_screen.onkey(player.forward1,"Up")



game = True
while game:
    time.sleep(0.1)
    my_screen.update()
    if random.randint(1, 6) == 1:
        box = Racer()
        box.genrate()
        list_box.append(box)
    for box_j in list_box:
        box_j.go()
        if player.distance(box_j)<20:
            game = False
            score.game_over()

    #finish line
    if player.finish_line():
            score.increment()
            score.show()
            player.start()
            day_23_adv_turtle.racer.I+=10




















my_screen.exitonclick()