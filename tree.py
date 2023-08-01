import turtle
from turtle import colormode
from random import randint
t=turtle.Turtle()
t.speed(0)
s=turtle.Screen()
s.title('sunset')
s.bgcolor('light goldenrod yellow')
r=randint(0,255)
g=randint(0,255)
b=randint(0,255)
colormode(255)
t.pensize(10)
t.pencolor('saddle brown')
t.penup()
t.goto(0,30)
t.pendown()
t.lt(90)
t.bk(130)

def line():
	t.pensize(20)
	t.seth(0)
	t.bk(700)
	t.fd(1400)
	t.bk(700)
	t.lt(90)
	t.pensize(3)
	t.fd(40)
line()
a=0

def tree(i,a):
	if i< a:
		return
	else:
		t.fd(i)
		#t.color('lime')
		#t.circle(2)
		t.color(r,g,b)
		t.lt(30)
		tree(3*i/4,a)
		t.rt(60)
		tree(3*i/4,a)
		t.lt(30)
		t.bk(i)
#tree(100 ,10)
t.bk(40)
def point(x,y):
	t.seth(0)
	t.penup()
	t.fd(x)
	t.pendown()
	t.lt(y)
point(80,90)


#tree 2
tree(25,3)



point(175,90)
#tree 3

tree(50,5)

point(240,90)

#tree 4
#tree(75,7)
point(575,90)

#tree 5
#tree(25,3)

point(175,90)

#tree 6
#tree(50,5)

point(240,90)

#tree7
#tree(75,7)

t.penup()
t.goto(-550,350)
t.pendown()
def sun():
	b=0
	t.begin_fill()
	while True:
		for i in range(4):
			for colors in['orange','gold']:
				t.color(colors)
				t.fd(70)
				t.rt(90)
		t.rt(5)
		b+=1
		if b>=300/5:
			break
	t.end_fill()
sun()
t.penup()
t.goto(-700,-100)
t.seth(0)
t.pendown()
t.color('pale turquoise')
def river():
	t.begin_fill()
	for i in range(2):
		t.fd(1400)
		t.rt(90)
		for j in range(1):
			t.fd(300)
			t.rt(90)
	t.end_fill()

river()
t.seth(270)
t.pensize(3)


turtle.mainloop()
