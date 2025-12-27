from graphics import *
import time
z = time.time()
w1 = GraphWin('Move', 400, 400)
w1.setCoords(0, 0, 400, 400)
t= Text(Point(200,200), "Avoid the red dot and stay between")
t1= Text(Point(200,180), "or within, the red rectangle")
t.draw(w1)
t1.draw(w1)
w1.getMouse()
time.sleep(1)
t.undraw()
t1.undraw()
x = Point(50,50)
c = Circle(x,5)
d =10
q = 1
p =0
p1=Point(10,10)
p3=Point(390,390)
p4 = Point(30,30)
p5 = Point(370,370)
r1 = Rectangle(p4,p5)
r = Rectangle(p1,p3)
r.setFill('red')
r1.setFill("white")
r.draw(w1)
r1.draw(w1)
c.setFill("blue")
c.draw(w1)
ai = Circle(Point(350,350),5)
ai.setFill('red')
ai.draw(w1)
last = time.time()
time.sleep(1)
while True:
	center = c.getCenter()
	centerX = center.getX()
	centerY = center.getY()
	if (centerX < p1.getX() or centerX > p3.getX()) or (centerY < p1.getY() or centerY > p3.getY()):
		break
	now = time.time()
	if now - last>=3:
		q+=1
		ai.undraw()
		c.undraw()
		r1.undraw()
		r.undraw()
		p1.move(20,20)
		p3.move(-20,-20)
		p4.move(20,20)
		p5.move(-20,-20)
		r = Rectangle(p1,p3)
		r.setFill("red")
		r1 = Rectangle(p4,p5)
		r1.setFill("white")
		r.draw(w1)
		r1.draw(w1)
		ai.draw(w1)
		c.draw(w1)
		p += 20
		last = now
	
	ac = ai.getCenter()
	cX = ac.getX()
	cY = ac.getY()
	if abs(centerX - cX) < 8 and abs(centerY - cY) < 8:
		break
	else:
		time.sleep(.02)
		if cX < centerX:
			ai.move(q,0)
		else:
			ai.move(-q,0)
		if cY < centerY:
			ai.move(0,q)
		else:
			ai.move(0,-q)
		time.sleep(.02)
	for i in range(2):
		a = w1.checkKey()
		if a =="w" and centerY < 390-p:
			c.move(0,d)
		if a =="s" and centerY > 10+p:
			c.move(0,-d)
		if a =="a" and centerX > 10+p:
			c.move(-d,0)
		if a =="d" and centerX < 390-p:
			c.move(d,0)




l = time.time()
a = l-z
t = Text(Point(200,200),"Your score is "+str(round(a)))
t.draw(w1)
w1.getMouse()

