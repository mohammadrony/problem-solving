import turtle

t = turtle.Turtle()

t.color('#2f2d22', 'blue')
t.begin_fill()
t.speed(15)
i,j = 1,0
for k in range(20):
    print(i, end=', ')
    t.circle(i/10, 90)
    m = i + j
    j = i
    i = m
t.end_fill()

turtle.done()