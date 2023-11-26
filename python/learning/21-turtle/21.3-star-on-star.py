import turtle


def draw_star(length):

    if(length<5): return
    global t1
    t1.begin_fill()
    for i in range(5):
        t1.forward(length)
        draw_star(length/4)
        t1.left(144)
    t1.end_fill()

t1 = turtle.Turtle()
t1.color('white', 'black')
t1.getscreen().bgcolor('cyan')

t1.speed('fast')
draw_star(400)


turtle.done()