import turtle
from math import *
k=20
turtle.speed(100000000000)
turtle.right(90)
turtle.pendown
for i in range(4):
    turtle.forward(8*k)
    turtle.right(60)
    turtle.forward(8*k)
    turtle.right(120)

for x in range(-10,3):
    for y in range(-13,1):
        turtle.penup
        turtle.goto(x*k,y*k)
        turtle.dot()

turtle.mainloop()
