import turtle
import math

t1 = turtle.Turtle()

t1.color("red", "cyan")
# t1.begin_fill()

t1.speed("fast")
for i in range(2000):
    t1.forward(10)
    t1.left(math.sin(i / 10) * 25)
    t1.left(30)
# t1.end_fill()

turtle.done()
