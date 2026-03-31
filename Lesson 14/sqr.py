import turtle
pen=turtle.Turtle()
pen.color("blue")
pen.fillcolor("yellow")
pen.begin_fill()
for i in range(4):
    pen.forward(100)
    pen.right(90)
pen.end_fill()
turtle.done()
