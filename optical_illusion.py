# optical illusion pattern 
# by Toushif1611

import turtle

# set screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

# set pen
pen =turtle.Turtle()
pen.hideturtle()
pen .speed(0)

colors=["red","purple","yellow","green","pink","orange"]

# main function
for i in range(300):
    pen.pencolor(colors[i%4])
    pen.width(i//100+1)
    pen.forward(i)
    pen.left(59)

screen.mainloop()