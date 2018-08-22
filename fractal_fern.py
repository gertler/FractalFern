#!/usr/bin/env python

from graphics import *
from numpy import random as nprand
from matrices import Transform


transform1 = Transform([[0, 0],[0, 0.16]], [0, 0])
transform2 = Transform([[0.85, 0.04],[-0.04, 0.85]], [0, 1.6])
transform3 = Transform([[0.2, -0.26],[0.23, 0.22]], [0, 1.6])
transform4 = Transform([[-0.15, 0.28],[0.26, 0.24]], [0, 0.44])
transforms = [transform1, transform2, transform3, transform4]

# Set up initial conditions
iterations = int(input('Enter the number of iterations (10000-20000 suggested): '))
x_min = -3
x_max = 3
y_min = -1
y_max = 11
win_size = 850

# Create the window and message
win = GraphWin('Fractal Fern', win_size, win_size)
win.setBackground('black')
win.setCoords(x_min, y_min, x_max, y_max)
message = Text(Point((x_max + x_min) / 2, y_max - 0.05*(y_max-y_min)), '')
message.setTextColor('purple')
message.setSize(14)
message.draw(win)

curr_point = Point(0,0)
new_point = Point(0,0)
division = iterations / 50
for i in range(0, iterations):
    if win.isClosed():
        break
    win.plot(curr_point.x, curr_point.y, 'green')
    if i % division == 0:
        message.setText('Iteration: ' + str(i) + ' / ' + str(iterations))

    transform = nprand.choice(transforms, p=[0.01, 0.85, 0.07, 0.07])
    new_point = transform.transform(curr_point)
    curr_point = new_point

if not win.isClosed():
    message.setText('Iteration: ' + str(iterations) + ' / ' + str(iterations) + '\nClick anywhere to quit')
    win.getMouse()
    win.close()
