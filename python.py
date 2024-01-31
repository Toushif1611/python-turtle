import turtle

turtle.bgcolor("black")

a=turtle.Turtle()
a.speed(0)

colors=["red","purple","yellow","green","pink","orange"]

for x in range(300):
    a.pencolor(colors[x%4])
    a.width(x//100+1)
    a.forward(x)
    a.left(59)

turtle.mainloop()