import turtle

painter = turtle.Turtle()

painter.pencolor("red")
for i in range(20):
    painter.forward(200)
    painter.left(150)
    painter.backward(100)
    painter.left(70)
turtle.done()