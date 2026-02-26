# star_pattern
# by toushif1611

import turtle

# set screen
s = turtle.Screen()
s.bgcolor("black")
s.tracer(0)

# set pen
a = turtle.Turtle()
a.color("white")
a.speed(0)
a.hideturtle()

# main turtle loop
while True:
    s.update()
    for i in range(200):
        a.forward(120)
        a.left(60)

    a.left(30)

s.mainloop()