#!/usr/bin/env python

from graphics import *
from random import *

def mmult(vect1, vect2):
    return sum(z[0]*z[1] for z in zip(vect1,vect2))


matrix_f1 = [
    [0.0, 0.0],
    [0.0, 0.16]
]
delta_f1 = [0.0, 0.0]

matrix_f2 = [
    [0.85, 0.04],
    [-0.04, 0.85]
]
delta_f2 = [0.0, 1.6]

matrix_f3 = [
    [0.20, -0.26],
    [0.23, 0.22]
]
delta_f3 = [0.0, 1.6]

matrix_f4 = [
    [-0.15, 0.28],
    [0.26, 0.24]
]
delta_f4 = [0.0, 0.44]


def f1(old_x, old_y):
    new_x = mmult([old_x, old_y], matrix_f1[0]) + delta_f1[0]
    new_y = mmult([old_x, old_y], matrix_f1[1]) + delta_f1[1]
    return new_x, new_y


def f2(old_x, old_y):
    new_x = mmult([old_x, old_y], matrix_f2[0]) + delta_f2[0]
    new_y = mmult([old_x, old_y], matrix_f2[1]) + delta_f2[1]
    return new_x, new_y


def f3(old_x, old_y):
    new_x = mmult([old_x, old_y], matrix_f3[0]) + delta_f3[0]
    new_y = mmult([old_x, old_y], matrix_f3[1]) + delta_f3[1]
    return new_x, new_y


def f4(old_x, old_y):
    new_x = mmult([old_x, old_y], matrix_f4[0]) + delta_f4[0]
    new_y = mmult([old_x, old_y], matrix_f4[1]) + delta_f4[1]
    return new_x, new_y


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

curr_x_y = 0, 0
new_x_y = 0, 0
division = iterations / 50
for i in range(0, iterations):
    if win.isClosed():
        break
    win.plot(curr_x_y[0], curr_x_y[1], 'green')
    if i % division == 0:
        message.setText('Iteration: ' + str(i) + ' / ' + str(iterations))

    num = randint(1, 100)
    if num <= 2: # 1
        new_x_y = f1(curr_x_y[0], curr_x_y[1])
    elif num <= 86: # 86
        new_x_y = f2(curr_x_y[0], curr_x_y[1])
    elif num <= 93: # 93
        new_x_y = f3(curr_x_y[0], curr_x_y[1])
    else:
        new_x_y = f4(curr_x_y[0], curr_x_y[1])

    curr_x_y = new_x_y

if not win.isClosed():
    message.setText('Iteration: ' + str(iterations) + ' / ' + str(iterations) + '\nClick anywhere to quit')
    win.getMouse()
    win.close()