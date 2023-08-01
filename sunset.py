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

def tree(i):
	if i<10:
		return
	else:
		t.fd(i)
		t.color('lime')
		t.circle(2)
		t.color('saddle brown')
		t.lt(30)
		tree(3*i/4)
		t.rt(60)
		tree(3*i/4)
		t.lt(30)
		t.bk(i)
tree(100)


t.bk(40)
t.seth(0)
t.penup()
t.fd(80)
t.pendown()
t.lt(90)
def tree_2(s):
	t.color('light coral')
	if s<3:
		return
	else:
		t.fd(s)
		t.lt(30)
		tree_2(3*s/4)
		t.rt(60)
		tree_2(3*s/4)
		t.lt(30)
		t.bk(s)
tree_2(25)


t.seth(0)
t.penup()
t.fd(175)
t.pendown()
t.lt(90)
def tree_3(s):
	t.color('dark cyan')
	if s<5:
		return
	else:
		t.fd(s)
		t.lt(30)
		tree_3(3*s/4)
		t.rt(60)
		tree_3(3*s/4)
		t.lt(30)
		t.bk(s)
tree_3(50)


t.seth(0)
t.penup()
t.fd(240)
t.pendown()
t.lt(90)
def tree_4(s):
	t.color('medium slate blue')
	if s<7:
		return
	else:
		t.fd(s)
		t.lt(30)
		tree_4(3*s/4)
		t.rt(60)
		tree_4(3*s/4)
		t.lt(30)
		t.bk(s)
tree_4(75)


t.seth(0)
t.penup()
t.bk(575)
t.pendown()
t.lt(90)
def tree_5(s):
	t.color('light coral')
	if s<3:
		return
	else:
		t.fd(s)
		t.lt(30)
		tree_5(3*s/4)
		t.rt(60)
		tree_5(3*s/4)
		t.lt(30)
		t.bk(s)
tree_5(25)


t.seth(0)
t.penup()
t.bk(175)
t.pendown()
t.lt(90)
def tree_6(s):
	t.color('dark cyan')
	if s<5:
		return
	else:
		t.fd(s)
		t.lt(30)
		tree_6(3*s/4)
		t.rt(60)
		tree_6(3*s/4)
		t.lt(30)
		t.bk(s)
tree_6(50)


t.seth(0)
t.penup()
t.bk(240)
t.pendown()
t.lt(90)
def tree_7(s):
	t.pencolor('medium slate blue')
	if s<7:
		return
	else:
		t.fd(s)
		t.lt(30)
		tree_7(3*s/4)
		t.rt(60)
		tree_7(3*s/4)
		t.lt(30)
		t.bk(s)
tree_7(75)

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
def root(j):
	if j<5:
		return
	else:
		t.fd(j)
		t.lt(30)
		root(3*j/4)
		t.rt(60)
		root(3*j/4)
		t.lt(30)
		t.bk(j)
#root(50)


turtle.mainloop()
