#3D illusion pattern 
#by ToushifA_1611

import turtle

#set screen
s=turtle.Screen()
s.bgcolor("black")
s.title("3D illusion pattern")

#pen
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)

for i in range(120):
    pen.forward(i)
    pen.left(90)
    pen.circle(i , 60)
    pen.right(90)
    pen.hideturtle()

s.mainloop()