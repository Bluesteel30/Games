from graphics import *
import time
#Stores the time that the program is run

#creates the window and the neccasary instructions
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

#Creates a circle object at 50,50 with radius 5 this is the user
x = Point(50,50)
c = Circle(x,5)\

#User speed (Technically how many pixels it travels) starts at 5 and ai at 1
d = 5
q = 1
p = 0

"""Creates two rectangles one larger and one smaller, the larger one is white and the smaller is red, 
with the red infront to create a red boarder that repersents the danger zone which is the area which will be shrunk from the map
and if you are in that area then you lose"""
p1=Point(10,10)
p3=Point(390,390)
p4 = Point(30,30)
p5 = Point(370,370)
r1 = Rectangle(p4,p5)
r = Rectangle(p1,p3)
#Draws the rectangles and the users circle
r.setFill('red')
r1.setFill("white")
r.draw(w1)
r1.draw(w1)
c.setFill("blue")
c.draw(w1)
points = 0
# ai is the Circle that is chasing the user
ai = Circle(Point(350,350),5)
ai.setFill('red')
ai.draw(w1)
last = time.time()
# 1 second delay before the game starts
time.sleep(1)

#handles key input
keys = set()

def key_down(e):
    keys.add(e.keysym.lower())

def key_up(e):
    keys.remove(e.keysym.lower())
w1.bind_all("<KeyPress>",  key_down)
w1.bind_all("<KeyRelease>",key_up)

while True:
	center = c.getCenter()
	centerX = center.getX()
	centerY = center.getY()
	if (centerX < p1.getX() or centerX > p3.getX()) or (centerY < p1.getY() or centerY > p3.getY()):
		break
	now = time.time()
	if now - last>=3:
		#q is how many pixels the ai moves. It increases every 3 seconds
		q+=2
		#user speed increases as well but less than the ai. I could just do q+=1 but it is more fun if both speed up
		d+=1
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
		points+=q
	
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
		# takes key input and moves according to wasd
	for i in range(2):
		if "w" in keys and centerY < 390-p:
			c.move(0,d)
		if "s" in keys and centerY > 10+p:
			c.move(0,-d)
		if "a" in keys and centerX > 10+p:
			c.move(-d,0)
		if "d" in keys and centerX < 390-p:
			c.move(d,0)





stri= "Your score is " + str(points)
print(stri)
t = Text(Point(200,200),stri)
t.draw(w1)
w1.getMouse()

