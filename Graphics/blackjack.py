#Dante Dante 
import random
from graphics import *
from blackjacklogic import *

w1 = GraphWin('Black Jack', 400, 400)
w1.setBackground("green")

def drawHand(window, hand, point):
    x = point.getX()
    y = point.getY()
    a = 0
    h = 0
    for card in hand:
        if card[:2] == '10':
            card = 't'+card[-1]
        p1 = Point(x+a,y)
        i = Image(p1,"C:/Users/ldion/Coding/Python/Games/Graphics/cards/" + card + ".gif")
        images.append(i)
        i.draw(w1)
        a += 50
    return(images)

r1 = Rectangle(Point(200,200), Point(100,100))
r1.setFill("blue")
r1.draw(w1)
r2 = Rectangle(Point(200,200), Point(300,100))
r2.setFill("white")
r2.draw(w1)
p = Text(Point(250,150),"Stay")
p.draw(w1)
user_prompt = Text(Point(150,150),"Hit")
user_prompt.draw(w1)
deal(deck,2,u)
deal(deck,2,z)
q = [z[0],'b']
drawHand(w1,u, Point(200,300))
drawHand(w1,q, Point(50,50))


q = w1.getMouse()
while ((q.getX() < 200 and q.getX() > 100) and (q.getY() < 200 and q.getY() > 100)):
    deal(deck,1,u)
    drawHand(w1,u, Point(200,300))
    q = w1.getMouse()
while not((q.getX() < 300 and q.getX() > 200) and (q.getY() < 200 and q.getY() > 100)):
    q = w1.getMouse()
computer(z)
drawHand(w1,z,Point(50,50))
t = winner(z,u)
t.draw(w1)



q = w1.getMouse()


