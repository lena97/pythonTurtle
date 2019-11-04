
## Turtles
## Authors:
## Lena Nejad
## Ramneet Brar
## November 7, 2018

## This program usses Python Turtles to implement a graphic representation of our creation
## Obviously we both love Tesla so decided to create an animation that showed our love towards the car <3

## Very proud of our creation here (:
## However, have to admit getting those edges to form properly like the logo is very hard, maybe in the future if time allows, we will modify 

#FUCNTIONS 
def draw_line (width, height):
    t.pensize (20)
    t.color ('grey')
    t.forward(width)
    t.backward(width / 2)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width / 2)
    t.backward(width)
    t.end_fill()
    
    

def curves():
    for i in range(200):
            t.right(1)
            t.forward(1)
            

def draw_heart ():
    t.pensize (7)
    color= random.choice(colors)
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.left(140)
    t.forward(111.65)
    curves()

    t.left(120)
    curves()
    
    t.forward(111.65)
    t.end_fill()
    

def drawSquare(sideLen):
    for i in range(4):
        t.pensize (10)
        color=random.choice(colors)
        t.color(color)
        t.backward(sideLen)
        t.right(90)
    return

def drawRedTriangle(length,width):
    t.color('red')
    t.fillcolor('red')
    t.begin_fill()
    t.forward(width)
    t.right(105)
    t.forward(length)
    t.right(152)
    t.forward(length-2)
    t.end_fill()
    return

def drawCurve(angle,forward,left):
    for i in range(angle):
        t.forward(forward)
        t.left(left)
    return


# TOP LEVEL

import turtle as t
import random
t.speed(5)

t.delay(5)


colors  = ["light green","blue","orange","purple","pink","yellow","cyan"]
t.penup()
t.backward(300)
t.pendown()

draw_line (100, 200)
t.penup()
t.right(180)
t.forward(100)
t.pendown()


draw_heart()
t.penup()
t.left(140)
t.forward(250)
t.left(90)
t.forward(150)
t.right(90)
t.pendown()


#bottom triangle
drawRedTriangle(200,70)

#left side of wing
t.begin_fill()
t.left(77)
t.forward(30)
drawCurve(42,1,2)
t.right(110)
drawCurve(32,2,-1)
t.right(100)
drawCurve(25,5,-1)
t.right(40)
t.forward(55)
t.end_fill()

#moving back to centre
t.left(43)
t.forward(45)

#right side of wing
t.begin_fill()
t.forward(30)
drawCurve(42,1,-2)
t.left(110)
drawCurve(32,2,1)
t.left(100)
drawCurve(25,5,1)
t.left(45)
t.forward(55)
t.end_fill()

#moving to upper semi, (pen-up)
t.penup()
t.right(180)
t.forward(55)
t.right(45)
drawCurve(25,5,-1)
t.left(75)
drawCurve(10,2,1)
t.left(90)

t.pendown()

#drawing upper semi
t.width(25)
t.penup()
drawCurve(2,6,0.95)
t.pendown()

drawCurve(55,6,0.95)
t.penup()
t.right(90)
t.fd(370)
t.left(63)
t.fd(190)
t.pendown()

drawSquare (720)

