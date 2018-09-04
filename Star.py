from turtle import *
colors = ['blue', 'cyan', 'blue', 'cyan', 'blue', 'cyan']
for x in range(50):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    backward(x)
    left(150)
    width(x / 100 + 1)
    forward(200)
    right(150)
    forward(100)
    right(200)
    width(x / 100 + 1)