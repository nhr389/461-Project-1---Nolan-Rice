import random

#iterates through each card value and adds one for each suit to a deck list
def buildDeck():
    deck = []
    for x in range(13):
        if x == 9:
            x="J"
        elif x == 10:
            x="Q"
        elif x== 11:
            x="K"
        elif x== 12:
            x="A"
        else:
            x = str(x+2)
        deck.extend([x+"S", x+"C", x+"H", x+"D"])
    return deck

#iterates through a hand to tally high cards and distribution
def countPoints(hand):
    score = 0
    suits = {"spades":0, "clubs":0, "hearts":0, "diamonds":0}
    for x in hand:
        if x[0] == "J":
            score +=1
        elif x[0] == "Q":
            score +=2
        elif x[0] == "K":
            score +=3
        elif x[0] == "A":
            score +=4

        if x[1] == "S":
            suits["spades"] +=1
        elif x[1] == "C":
            suits["clubs"] +=1
        elif x[1] == "H":
            suits["hearts"] +=1
        elif x[1] == "D":
            suits["diamonds"] +=1

    for x in suits:
        if suits[x] == 0:
            score +=5
        elif suits[x] == 1:
            score +=2
        elif suits[x] == 2:
            score +=1
    return score

#creates a list of 13 cards from a larger deck list
def draw(deck):
    hand = []
    for x in range(13):
        hand.append(deck[x])
    return hand

#iterates through a hand list to show users a hand
def printHand(hand):
    for x in range(13):
        print (deck[x], end=" ")
    print("\n")

#simulates n number of partner hands and prints the outcomes with the player's score
def simulate(deck, playerScore, size):
    pas = 0
    part = 0
    game = 0
    small = 0
    grand = 0
    for x in range(size):
        random.shuffle(remainingDeck)
        partnerHand = draw(remainingDeck)
        score = countPoints(partnerHand) + playerScore
        if score < 20:
            pas +=1
        elif 19 < score < 26:
            part +=1
        elif 25 < score < 32:
            game +=1
        elif 31 < score < 36:
            small +=1
        elif score > 35:
            grand +=1
    print("Pass: ", round(100*(pas/size), 3), "%")
    print("Part: ", round(100*part/size, 3), "%")
    print("Game: ", round(100*game/size, 3), "%")
    print("Small Slam: ", round(100*(small/size), 3), "%")
    print("Grand Slam: ", round(100*(grand/size), 3), "%")
    
#displays info to user and runs the simulation
deck = buildDeck()
while True:
    random.shuffle(deck)
    playerHand = draw(deck)
    print("Here is your hand:")
    printHand(playerHand)
    playerScore = countPoints(playerHand)
    print ("This hand is worth ", playerScore, " points.")
    remainingDeck = [x for x in deck if x not in playerHand]
    print ("Running simulation.....\n")
    simulate(remainingDeck, playerScore, 500)
    answer = input("\nAnother hand [Y/N]? ")
    if answer.capitalize() == "Y":
        continue
    else:
        break