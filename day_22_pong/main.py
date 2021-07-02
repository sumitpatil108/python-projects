from turtle import Turtle,Screen
from day_22_pong.paddle import Paddle
from day_22_pong.ball import Ball
from day_22_pong.score import Score
import time
POSITION_PADDLE = [(350,0),(-350,0)]

my_screen = Screen()
my_screen.title("Pong")
my_screen.bgcolor("black")
my_screen.setup(height=600,width=800)
my_screen.tracer(0)
paddle_box = []

paddle1 = Paddle(POSITION_PADDLE[0])
paddle2 = Paddle(POSITION_PADDLE[1])

ball = Ball()
score = Score()

my_screen.listen()
my_screen.onkey(paddle1.go_up,"Up")
my_screen.onkey(paddle1.go_dowen,"Down")
my_screen.onkey(paddle2.go_up,"w")
my_screen.onkey(paddle2.go_dowen,"s")





is_game = True
while is_game:
    time.sleep(0.1)
    my_screen.update()
    ball.move()
    print(ball.ycor())
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.change_angle()

    if ball.distance(paddle1)<50 and ball.xcor()>320:
        ball.x+=5
        ball.change_angle_x()
        score.score_r()

    if ball.distance(paddle2)<50 and ball.xcor()<-320:
        ball.change_angle_x()
        score.score_l()
        ball.x+=5


    if ball.xcor()>380:
        is_game = False
        score.score_l()
        score.game_over()
        ball.reset_position()
    if ball.xcor()<-380:
        is_game = False
        score.score_r()
        score.game_over()
        ball.reset_position()







my_screen.exitonclick()