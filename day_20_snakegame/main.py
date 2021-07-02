from turtle import Screen
from day_20_snakegame.snake import Snake
from day_20_snakegame.food import Food
from day_20_snakegame.scoreboard import Score
import day_20_snakegame.scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food)< 18:
        food.refresh()
        score.detect_colission_score()
        snake.update_snake()
    if snake.head.xcor()>290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False

        score.game_over()
    #if snake head collide with tail
    for seg in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()