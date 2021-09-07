#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.clear()

#The positions
nose=(19,69)
finger=(111,-90)
left_eye=(-15,108)
leftForhead=(-25,185)
rightForhead=(33,190)
chin=(25,10)

turtle.shape("turtle")

#Clown nose color and shape
turtle.penup()
turtle.goto(nose)
turtle.pendown()
turtle.color("red","black")
turtle.pensize(5)
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

#Draw the wand in purple color and different stroke width
turtle.penup()
turtle.color("purple")
turtle.goto(finger)
turtle.pendown()
turtle.pensize(20)
turtle.forward(150)

#Draw the polygon and unfilled with pink stroke color by using RGB code 
turtle.pensize(15)
turtle.color(255,192,203)
turtle.forward(50)
turtle.left(72)
turtle.forward(50)
turtle.left(72)
turtle.forward(50)
turtle.left(72)
turtle.forward(50)
turtle.left(72)
turtle.forward(50)
turtle.left(72)
turtle.penup()

turtle.goto(0,10)
turtle.pendown()
turtle.color("grey")
turtle.begin_fill()
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)
turtle.end_fill()
turtle.penup()



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
