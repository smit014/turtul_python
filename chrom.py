from turtle import *
bgcolor('black')
pencolor('white')
pensize(3)
penup()
goto(0,-100)
pendown()
def c1(a,b,col,cr):
	begin_fill()
	color(col)

	circle(a,b)
	lt(60)
	fd(96)
	rt(90)
	fd(3)
	lt(90)
	bk(96)
	rt(60)
	
	end_fill()
c1(170,120,'yellow','red')
c1(170,120,'red','green')
c1(170,120,'green','yellow')
def c2(a,b,col):
	pencolor(col)
	circle(a,b)
c2(100,120,'yellow')
c2(100,120,'red')
c2(100,120,'green')

pencolor('white')
pensize(5)
penup()
lt(90)
fd(5)
rt(90)
pendown()
circle(95)
penup()
lt(90)
fd(5)
rt(90)
pendown()
color("blue")
begin_fill()
circle(90)
end_fill()
#hideturtle()
done()