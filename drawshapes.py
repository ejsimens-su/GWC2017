from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(300,300)

### Write your code below:
sides = int(input('How many sides do you want?'))
degrees = 360 / sides
t.fillcolor('pink')

def draw_a_shape():
    for i in range(sides):
        t.pd()
        t.forward(100)
        t.right(degrees)
        t.fillcolor()
draw_a_shape()

#question = input('Would you like to draw a shape?')
#if question == 'yes':
#    draw_a_shape()


# Close window on click.
exitonclick()
