import turtle
s=turtle.Screen()
s.bgcolor("black")
s.title("virus")

a=turtle.Turtle()
a.color("white")
a.speed(0)

for i in range(200):
    a.forward(i)
    a.left(i+1)
    a.hideturtle()


s.mainloop()