#Randomly players gather the cards. As many as the player can gather
import random


def player1_pick():
    random_card1 = random.choice(list(deck))
    player1.add(random_card1)
    deck.remove(random_card1)


def player2_pick():
    random_card2 = random.choice(list(deck))
    player2.add(random_card2)
    deck.remove(random_card2)

def play():
    while len(deck)>0:
        if random.randint(1, 2)==1:
            player1_pick()
        else:
            player2_pick()


kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}

deck = {(k, n) for k in kind for n in number}
player1 = set()
player2 = set()

play()
print(len(player1))
print(len(player2))
print(deck)