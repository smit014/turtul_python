from turtle import *
bgcolor('ivory')
pensize(3)
color('black')
def Eye_1():
	penup()
	goto(-682,300)
	pendown()
	rt(45)
	for i in range(85):
		lt(1)
		fd(3)
	seth(135)
	for i in range(42):
		lt(1)
		fd(3)
	circle(45,180)
	begin_fill()
	circle(20)
	end_fill()
	circle(45,180)
	for i in range(43):
		lt(1)
		fd(3)
#Eye_1()

def eye_2(x,y):
	penup()
	goto(x,y)
	pendown()
	def eye():
		begin_fill()
		circle(80)
		end_fill()
		penup()
		lt(90)
		fd(35)
		seth(0)
		pendown()
		color("sea green")
		begin_fill()
		circle(45)
		end_fill()
		penup()
		lt(90)
		fd(17)
		seth(0)
		pendown()
		color('black')
		begin_fill()
		circle(25)
		end_fill()
		color('white')
		begin_fill()
		lt(93)
		penup()
		fd(50)
		pendown()
		circle(10)
		end_fill()
	eye()
	penup()
	goto(x,y)
	seth(0)
	fd(200)
	pendown()
	eye()
#eye_2(0,0)

def sage_eye(a,x,y):
	def eyebrow():
		color('orange red')
		begin_fill()
		penup()
		goto(x,y)
		pendown()
		seth(a)
		rt(12)
		for i in range(28):
			lt(1)
			fd(8)
		lt(25)
		for i in range(43):
			lt(1)
			fd(8)
		lt(75)
		for i in range(89):
			lt(1)
			fd(5)
		end_fill()
		color('black')
		begin_fill()
		penup()
		goto(x,y)
		pendown()
		seth(a)
		rt(11)
		for i in range(26):
			lt(1)
			fd(8)
		lt(42)
		for i in range(29):
			lt(1)
			fd(8)
		lt(70)
		for i in range(107):
			lt(1)
			fd(4)
		end_fill()
		color('antique white')
		begin_fill()
		penup()
		goto(x,y)
		pendown()
		seth(a)
		rt(8)
		for i in range(25):
			lt(1)
			fd(8)
		lt(45)
		for i in range(25):
			lt(1)
			fd(8)
		lt(75)
		for i in range(95):
			lt(1)
			fd(4)
		end_fill()
		penup()
		goto(x,y)
		seth(160)
		fd(150)
		pendown()
		fillcolor('dark orange')
		pencolor('black')
		begin_fill()
		rt(10)
		fd(20)
		bk(20)
		lt(10)
		rt(170)
		for i in range(34):
			fd(0.8)
			lt(1.5)
		fd(180)
		lt(3)
		fd(250)
		for i in range(3):
			rt(3)
			fd(15)
		seth(180)
		fd(45)
		lt(45)
		for i in range(7):
			fd(65)
			rt(0.7)
		for i in range(20):
			fd(0.9)
			rt(3)
		end_fill()
	eyebrow()
	def eyeball():
		color('black')
		penup()
		goto(x,y)
		seth(75)
		fd(188)
		pendown()
		seth(210)
		pensize(7)
		circle(70)
		penup()
		lt(90)
		fd(4)
		seth(210)
		pendown()
		color('dark goldenrod')
		begin_fill()
		pensize(6)
		circle(66)
		end_fill()
		penup()
		color('orange')
		lt(90)
		fd(5)
		pendown()
		seth(210)
		begin_fill()
		circle(60)
		end_fill()
		penup()
		color('gold')
		lt(90)
		fd(6)
		pendown()
		seth(210)
		begin_fill()
		circle(53.5)
		end_fill()
		penup()
		lt(55)
		fd(40)
		seth(0)
		pendown()
		color('black')
		begin_fill()
		for i in range(2):
			fd(55)
			rt(90)
			fd(20)
			rt(90)
		penup()
		fd(2)
		rt(90)
		fd(5)
		end_fill()
		pendown()
		color('white')
		for i in range(2):
			fd(5)
			rt(90)
			fd(10)
			rt(90)
		seth(120)
		pencolor('black')
		penup()
		fd(20)
		pendown()
		fd(10)
		seth(20)
		penup()
		fd(20)
		rt(88)
		pendown()
		fd(15)
	eyeball()
sage_eye(0,-100,-100)

pensize(3)
	
hideturtle() 
done()