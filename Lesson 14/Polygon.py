import turtle
screen=turtle.Screen()
screen.bgcolor("orange")
screen.setup(width=600, height=600)
polygon=turtle.Turtle()
ns=6
sl=100
a=360/ns
for i in range(ns):
    polygon.forward(sl)
    polygon.right(a)
turtle.done()