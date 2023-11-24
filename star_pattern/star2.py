import turtle

s = turtle.Screen()
s.bgcolor("black")
s.tracer(0)

a = turtle.Turtle()
a.color("white")
a.speed(0)
a.hideturtle()

while True:
    s.update()
    for i in range(120):
        a.forward(120)
        a.left(120)

    a.left(30)

s.mainloop()