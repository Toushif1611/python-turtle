#create virus
# by ToushifA-1611

import turtle

#set screen
s=turtle.Screen()
s.bgcolor("black")
s.title("virus")

#pen
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)

#virus body
for i in range(200):
    pen.forward(i)
    pen.left(i+1)
    pen.hideturtle()


s.mainloop()