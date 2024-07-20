import time
from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard


screen = Screen()
food = Food()
scoreboard = ScoreBoard()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.snake_up,"Up")
screen.onkey(snake.snake_down,"Down")
screen.onkey(snake.snake_left,"Left")
screen.onkey(snake.snake_right,"Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_add()

    #detect collison with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
















screen.exitonclick()