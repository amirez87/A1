import turtle

spiral = turtle.Turtle()

for i in range(11):
    spiral.forward(i * 20)
    spiral.right(150)
    spiral.forward(100)
    spiral.right(100)
    spiral.backward(200)

turtle.done()