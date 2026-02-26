# 3D illusion pattern 
# by Toushif1611

import turtle

# set screen
s=turtle.Screen()
s.bgcolor("black")
s.title("3D illusion pattern")

# set pen
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)

# main loop
for i in range(120):
    pen.forward(i)
    pen.left(90)
    pen.circle(i , 60)
    pen.right(90)
    pen.hideturtle()

s.mainloop()