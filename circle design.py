import turtle
from random import randint
from turtle import colormode
t=turtle.Turtle()
s=turtle.Screen()
t.speed(0)
s.bgcolor('black')
r=randint(0,255)
g=randint(0,255)
b=randint(0,255)
colormode(255)
t.pencolor(r,b,g)

t.pensize(2)
def drawcircle(radius):
    for i in range(10):
        t.circle(radius)
        radius=radius-4
   
def drawdesign():
    for i in range(11):
        drawcircle(150)
        t.right(32)
drawdesign()
turtle.done()