from turtle import Screen
import time
from scoreboard import ScoreBoard
from snake_body import Snake
from food import Food
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
lucas=Snake()
food=Food()
score=ScoreBoard()
screen.onkey(lucas.turn_up,"Up")
screen.onkey(lucas.turn_down,"Down")
screen.onkey(lucas.turn_left,"Left")
screen.onkey(lucas.turn_right,"Right")
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    lucas.move()
    if lucas.head.distance(food)<12:
        food.refresh()
        score.refresh()
        lucas.extend_body()
    if lucas.head.xcor()>290 or lucas.head.xcor()<-290 or lucas.head.ycor()>290 or lucas.head.ycor()<-290:
        score.reset_score()
        lucas.reset_snake()
    for parts in lucas.snake[1:]:
        if lucas.head.distance(parts)<10:
            score.reset_score()
            lucas.reset_snake()
screen.exitonclick()