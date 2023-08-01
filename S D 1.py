import turtle
from random import randint
from turtle import colormode
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
r=randint(0,255)
g=randint(0,255)
b=randint(0,255)
colormode(255)
t.pencolor(r,b,g)
#t.pencolor('red')
t.speed(0)
t.penup()
t.goto(0,150)
t.pendown()
b=0
c=0
while True:
	for i in range(4):
		t.fd(125)
		t.rt(90)
	t.rt(5)
	b+=1
	if b>=360/5:
		t.rt(45)
		t.fd(50)

		b=0
		c+=1
		if c>=8:		
			break
t.hideturtle()

turtle.done()