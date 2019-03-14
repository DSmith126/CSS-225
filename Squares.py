#Deshawn Smith
#2/28/2019

#Draws a set of concentric squares

import turtle

def drawSquare(t, SZ):
    for i in range(4):
        t.forward(SZ)
        t.left(90)

wn = turtle.Screen()

Deshawn = turtle.Turtle()
Deshawn.color("red")

size = [20, 40, 60, 80, 100]

for x in size:
    drawSquare(Deshawn, x)
    Deshawn.penup()
    Deshawn.backward(10)
    Deshawn.right(90)
    Deshawn.foward(10)
    Deshawn.left(90)
    Deshawn.pendown()


#drawSquare(Deshawn, 100)




wn.exitonclick()
