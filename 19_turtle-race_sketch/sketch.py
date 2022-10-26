from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()


def move_forwards():
    arrow.forward(10)

def move_backwards():
    arrow.backward(10)

def turn_left():
    new_heading = arrow.heading() + 10
    arrow.setheading(new_heading)

def turn_right():
    new_heading = arrow.heading() - 10
    arrow.setheading(new_heading)

def clear():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
