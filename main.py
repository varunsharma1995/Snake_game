from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score_card = 0
race_is_on = True
score = Scoreboard()

while race_is_on:
    screen.update()
    time.sleep(.1)
    screen.title(score_card)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_calculator()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        race_is_on = False
        score.game_over()

    for segments in snake.seg[1::]:
        if snake.head.distance(segments) < 10:
            score.game_over()
            race_is_on = False
    snake.move()
print(score_card)
screen.exitonclick()
