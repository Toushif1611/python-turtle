import turtle

s=turtle.Screen()
s.bgcolor("black")

a=turtle.Turtle()
a.color("white")
a.speed(0)

for i in range(120):
    a.forward(i)
    a.left(90)
    a.circle(i , 60)
    a.right(90)
    a.hideturtle()


s.mainloop()