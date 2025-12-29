import random
from graphics import *
suits = ["c","d","h","s"]
deck = []
l = []
u = []
z = []
images = [] 
ranks = [2,3,4,5,6,7,8,9,10,'a','j','q','k']
for i in suits:
    for d in ranks:
        deck.append(str(d)+i)

def deal(cards: list, num: int, user_hand: list):    
    for i in range(num):
        x = random.choice(cards)
        user_hand.append(x)
        cards.remove(x)
    return user_hand

def hand_value(user_hand: list):
    sum0 = 0
    sum1 = 0
    li = []
    for i in user_hand:
        li.append(i[0])
        if i[0].isalpha():
            if i[0] == 'a': 
                sum0 += 1
                sum1 = 10
            else:
                sum0 += 10
        elif i[:2] != '10':
            sum0 += int(i[0])
        else:
            sum0 += 10
    if 'a' in li:
        sum1 += sum0
    else:
        sum1 = sum0
    return(sum0, sum1)

def blackjack(hand: list):
    face = ['j','q','k']
    if len(hand) != 2:
        return False
    if ((hand[0][0] == 'a') or (hand[1][0] == 'a')):
        if hand[0][0] in face or hand[1][0] in face:
            return True



def computer(hand: list):
    sum0, sum1 = hand_value(hand)
    while (sum1 < 17 and sum0 < 17):
        deal(deck,1,hand)
        sum0, sum1 = hand_value(hand)
    while (sum1 < 17 and sum0 > 21):
        deal(deck,1,hand)
        sum0, sum1 = hand_value(hand)
    while (sum0 < 17 and sum1 > 21):
        deal(deck,1,hand)
        sum0, sum1 = hand_value(hand)
    


def winner(computer, user):
    l1 = []
    l2 = []
    c1, c2 = hand_value(computer)
    u1, u2 = hand_value(user)
    mc = max(c1,c2)
    if mc > 21:
        mc = min(c2,c1)
    if mc > 21:
        mc = 0
    uc = max(u2,u1)
    if uc > 21:
        uc = min(u2,u1)
    if uc > 21:
        uc = 0
    print(z)
    print(hand_value(computer),99,hand_value(user))
    print(mc,99,uc)
    if blackjack(computer):
        mc += 1
    if blackjack(user):
        uc += 1
    if mc > uc:
        t = Text(Point(150,220),"computer Wins")
    elif uc > mc:
        t= Text(Point(150,220),"User Wins")
    else:
        t = Text(Point(150,220)," Draw")
    return(t)

