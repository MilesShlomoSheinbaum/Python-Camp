"""import turtle

x = turtle.getscreen()

turtle.done()
"""

import turtle
import random
screen = turtle.Screen()
screen.setup(width=600, height=600)
print()
t = turtle.Turtle()
t._tracer(0)
t.speed(0)
t.penup()
t.right(90)

for x in range(0, 600, 30):
    t.goto(-270 + x, 300)
    t.pendown()
    t.forward(600)
    t.penup()
t.left(90)

for x in range(0, 600, 30):
    t.goto(-300, 270 - x)
    t.pendown()
    t.forward(600)
    t.penup()
t.forward(600)


t.penup()
t.goto(0, 0)
t.pendown()



#square = 30
def make_Square(x_coord, y_coord):

    listOfColors = [
        "green",
        "blue",
        "yellow",
        "red",
        "cyan",
        "maroon",
        "crimson",
        "firebrick"
    ]

    chosenColor = listOfColors[random.randint(0, len(listOfColors) - 1)]
    t = turtle.Turtle()
    t.penup()
    t.goto(x_coord, y_coord)
    t.fillcolor(chosenColor)
    t.begin_fill()
    for z in range(1, 5):
        t.forward(30)
        t.right(90)
    t.end_fill()
def generate_coords():
    xCoords = list(range(-300, 300, 30))
    random.shuffle(xCoords)
    print(len(xCoords))
    yCoords = list(range(-270, 330, 30))
    random.shuffle(yCoords)

    return xCoords, yCoords

# Finish later

xCoords, yCoords = generate_coords()
final = []
for x in range(len(xCoords)):
    for y in range(len(yCoords)):
        final.append((xCoords[x], yCoords[y]))
random.shuffle(final)
for x, y in final:
    make_Square(x, y)


#make a function that creates a square and fills them all with a different random color
#make a function with perameters x coordinate and y coordinate that calls the previous function 
turtle.done()