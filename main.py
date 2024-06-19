import time
from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# create a snake body
snake=Snake()
food=Food()
Scoreboard=scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Move the snake

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        Scoreboard.increase_score()

# create scoreboard
# detect collision wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        Scoreboard.reset()
        snake.reset()

# detect collision with tail
    for segment in snake.segments[1:]:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            Scoreboard.reset()
            snake.reset()


screen.exitonclick()
