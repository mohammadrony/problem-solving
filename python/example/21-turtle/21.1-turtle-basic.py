import turtle

t1 = turtle.Turtle()
t1.color("blue", "cyan")


t1.begin_fill()
t1.forward(100)
t1.left(90)
t1.back(20)
t1.forward(20)
t1.forward(100)
t1.left(90)
t1.forward(100)
t1.left(90)
t1.forward(100)
t1.end_fill()

t1.goto(-100, 0)
t1.penup()
t1.goto(-150, 50)
t1.pendown()
t1.color("red", "green")
t1.begin_fill()
t1.circle(50, 180, 4)
t1.end_fill()

turtle.done()
