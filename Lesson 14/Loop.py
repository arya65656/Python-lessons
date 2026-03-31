import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Square Spiral")
pen = turtle.Turtle()
pen.speed(10)
s = 5
while s>=0:
    pen.forward(s)
    pen.left(90)
    s += 5