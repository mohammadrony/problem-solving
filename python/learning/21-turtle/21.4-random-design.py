import turtle

t = turtle.Turtle()

t.color("#2f2d22", "blue")
t.begin_fill()
t.speed(15)
for i in range(40):
    t.left(130)
    t.forward(i * 4)
    t.circle(i, 180)
t.end_fill()

turtle.done()
