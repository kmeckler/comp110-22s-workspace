"""EX04 - Turtle Art. A serene temple: Day and Night!"""

__author__ = 730231293

from turtle import Turtle, colormode, done
from random import randint
colormode(255)
turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    turtle.speed(300)
    sky(turtle, -450, 0, "light blue")
    sky(turtle, -50, 0, "black")
    stars(turtle)
    building(turtle, 0, 0)
    roof(turtle, 0, 100)
    building(turtle, -300, 0)
    roof(turtle, -300, 100)
    roof_topper(turtle, 50, 200)
    ground(turtle, -450, 0)
    done()


def geometric_shape_repeater(turtle, x: int, y: int, forward: int, left: int, sides: int) -> None:
    """Allows shapes that are common in geometric art (i.e. rectangles, triangles, squares) to be drawn three times."""
    i: int = 0
    j: int = 0
    increment: int = 50
    while j < 3:
        turtle.color(142, 150, 174)
        turtle.begin_fill()
        while i < sides:
            turtle.forward(forward)
            turtle.left(left)
            i += 1
        turtle.end_fill()    
        turtle.penup()
        turtle.forward(increment)
        turtle.pendown()
        j += 1
        i = 0


def building(turtle, x: int, y: int) -> None:
    """Draws the square-shaped buildings by making use of geometric_shape_repeater."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    geometric_shape_repeater(turtle, 0, 0, 100, 90, 4)


def roof(turtle, x: int, y: int) -> None:
    """Draws the triangular-shaped roofs by making use of geometric_shape_repeater."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    geometric_shape_repeater(turtle, 0, 100, 100, 120, 3)


def roof_topper(turtle, x: int, y: int) -> None:
    """Adds three yellow circles to one of the serene temple buildings -- for light when it is dark out!"""
    i: int = 0
    increment: int = 50
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    while i < 3:
        turtle.color(215, 172, 0)
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x + increment, y)
        turtle.pendown()
        i += 1
        increment += increment


def ground(turtle, x: int, y: int) -> None:
    """Adds a line of green to the base of the buildings, representing the ground."""
    turtle.color(0, 87, 12)
    turtle.width(5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(800)


def sky(turtle, x: int, y: int, color: str) -> None:
    """Generates a square of color of choice to represent the sky."""
    i: int = 0
    turtle.color(color)
    turtle.penup()
    turtle.begin_fill()
    turtle.goto(x, y)
    turtle.pendown()
    while i < 4:
        turtle.forward(400)
        turtle.left(90)
        i += 1
    turtle.end_fill()


def stars(turtle) -> None:
    """Requirement: Try something fun! This function uses randint() and circle() to add stars to the night sky."""
    i: int = 0
    while i < 200:
        turtle.color("white")
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(randint(0, 600), randint(50, 600))
        turtle.circle(1)
        turtle.end_fill()
        i += 1


if __name__ == "__main__":
    main()