# star_pattern
# by toushifA_1611

import turtle

#set screen
s = turtle.Screen()
s.bgcolor("black")
s.tracer(0)

#pen
a = turtle.Turtle()
a.color("white")
a.speed(0)
a.hideturtle()

#main turtle loop
while True:
    s.update()
    for i in range(200):
        a.forward(120)
        a.left(90)

    a.left(30)

s.mainloop()