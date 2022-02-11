"""EX04 - Turtle Art. A serene temple: Day and Night!"""

__author__ = 730231293

from turtle import Turtle, colormode, done
colormode(255)


def main():
    turtle = Turtle()
    turtle.speed(5)
    sky(turtle, -450, 0, "light blue")
    sky(turtle, -50, 0, "black")
    building(turtle, 0, 0)
    roof(turtle, 0, 100)
    building(turtle, -300, 0)
    roof(turtle, -300, 100)
    ground(turtle, -400, 0)
    roof_topper(turtle, 50, 200)
    done()


def geometric_shape_repeater(turtle, x: int, y: int, forward: int, left: int, sides: int):
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


def building(turtle, x: int, y: int):
    """Draws the square-shaped buildings by making use of geometric_shape_repeater."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    geometric_shape_repeater(turtle, 0, 0, 100, 90, 4)


def roof(turtle, x: int, y: int):
    """Draws the triangular-shaped roofs by making use of geometric_shape_repeater."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    geometric_shape_repeater(turtle, 0, 100, 100, 120, 3)


def roof_topper(turtle, x: int, y: int):
    """Adds three yellow circles to one of the serene temple buildings -- for light when it is dark out!"""
    i: int = 0
    increment: int = 50
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    while i < 3:
        turtle.fill_color(215, 172, 0)
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x + increment, y)
        turtle.pendown()
        i += 1
        increment += increment


def ground(turtle, x: int, y: int):
    """Adds a line of green to the base of the buildings, representing the ground."""
    turtle.color(0, 87, 12)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(700)


def sky(turtle, x: int, y: int, color: str):
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


if __name__ == "__main__":
    main()