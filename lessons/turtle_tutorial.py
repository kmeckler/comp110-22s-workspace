"""Turtle tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

# leo.forward(50)
# leo.left(30)
# leo.right(40)

# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)

i: int = 0

leo.color(99, 204, 250)

leo.penup()
leo.goto(45, 60)
leo.pendown()

leo.begin_fill()

while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()


bob: Turtle = Turtle()
bob.color(1, 2, 250)
bob.penup()
bob.goto(45, 60)
bob.pendown()
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i += 1
side_length: float = 300 
side_length += 0.97
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(123)
    i = i + 1

done()