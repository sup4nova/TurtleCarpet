from turtle import *

def square(x, y, length):
    """Draws a filled square at position x, y with a given length."""
    up()
    goto(x, y)
    down()
    begin_fill()
    for _ in range(4):
        forward(length)
        left(90)
    end_fill()

def child_squares(x, y, length):
    """Returns the list of 8 smaller squares around the center."""
    return [
        (x + 2 * length // 3, y + length // 3, length // 3),  # East
        (x + 2 * length // 3, y + 2 * length // 3, length // 3),  # North-East
        (x + length // 3, y + 2 * length // 3, length // 3),  # North
        (x, y + 2 * length // 3, length // 3),  # North-West
        (x, y + length // 3, length // 3),  # West
        (x, y, length // 3),  # South-West
        (x + length // 3, y, length // 3),  # South
        (x + 2 * length // 3, y, length // 3),  # South-East
    ]

def sierpinski(x, y, length, depth):
    """Draws the Sierpinski carpet."""
    if depth == 0:
        square(x, y, length)
    else:
        # Skip the center and recursively draw on the 8 other areas
        for (nx, ny, nl) in child_squares(x, y, length):
            sierpinski(nx, ny, nl, depth - 1)

# Initialization
bgcolor("white")
color("black", "black")
speed(10)        # Set turtle's drawing speed
tracer(5)        

# Start drawing
initial_length = 243
depth = 4
sierpinski(-initial_length // 2, -initial_length // 2, initial_length, depth)

update()
done()
