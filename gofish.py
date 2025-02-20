#Danae Morrison, Nam Tran
import random
from random import randint
import time
#deck of cards
def all_numbers():
    deck_of_cards = []
    deck_of_cards += [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    deck_of_cards += [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    deck_of_cards += [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    deck_of_cards += [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    random.shuffle(deck_of_cards)
    return deck_of_cards


deck_of_cards = all_numbers()

def assign_cards(): #assign cards to players
    hand = []
    for i in range(0, 5):
        hand.append(deck_of_cards[0])
        del deck_of_cards[0]
    return hand

#variables
player1 = assign_cards()
player2 = assign_cards()
player3 = assign_cards()
sets1 = 0
sets2 = 0
sets3 = 0
asking_who = ""
cardnum = ""
current_player = "1"

#tests
print("Welcome to Gold Fish. Here are the following instructions on how to play the game:")
print()
time.sleep(2)

print("- We will be using a standard 52-card pack, each player will be given 5 cards.")
print()
time.sleep(2)

print("- When it's the player's turn they choose which player they would like to ask, and the card numbers they would like to take from the player range from 1-13.")
print()
time.sleep(2)

print("If the player guesses the correct card, the addressed player will have to hand all the requested cards. On the other hands, if the player gusses is incorrect. The addressed player will say 'Go Fish', and the player will have to pick a card from the deck of cards and it'll be the next player's turn ")
print()
time.sleep(2)

print("- However if the player pick up the same card they had guessed previous from the deck of cards they may continue their turn.")
print()
time.sleep(2)

print("- For ever four of a kind of cards, it will form a sets. That set will be remove from the player's deck.")
print()
time.sleep(2)

print("- The game end when the final card from the deck of cards is drawn. For 3 players each will have 5 cards total up to 15 cards. There will be 37 cards left in a standard 52-card pack.")
print()
time.sleep(2)

print("- The victor will be decided with the most sets.")
print()
time.sleep(5)

print("Player 1")
print(player1)
print()

asking_who = input("Who do you want to ask?:\n")
while "2" not in asking_who and "3" not in asking_who:
    print ("Your answer must have either 2 or 3 in it to represent asking Player 2 or Player 3.")
    asking_who = input("Who do you want to ask?:\n")
cardnum = input("What card do you want to ask for?:\n")
while (cardnum != "1" and cardnum != "2" and cardnum != "3" and cardnum != "4" and cardnum != "5" and cardnum != "6" and cardnum != "7" and cardnum != "8" and cardnum != "9" and cardnum != "10" and cardnum != "11" and cardnum != "12" and cardnum != "13" ) or cardnum not in player1:
    print ("The number has to be within the range of 1 to 13 and must be a card that you have in your hand.")
    cardnum = input("What card do you want to ask for?:\n")

while len(deck_of_cards) != 0: #game loops
    if len(player1) < 1:
        print ("Player 1 is out of the game.")
        current_player = "2"
    if current_player == "1" and len(player1) > 0:
        if "2" in asking_who:
            if cardnum in player2:
                print("Player 2: I have that card.")
                num_of_cards = 0
                i = 0
                while i != len(player2):
                    if player2[i] == cardnum:
                      num_of_cards += 1
                      del player2[i]
                    i += 1
                for i in range (num_of_cards):
                    player1.append(cardnum)
                player1 = sorted(player1)
                print("Player 1: ", player1) 
                current_player = "1"
                if len(player1) > 3:
                    for i in range(len(player1) - 3):
                        if player1[i] == player1[i + 1] and player1[i] == player1[i + 2] and player1[i] == player1[i + 3]:
                            sets1 += 1
                            print ("You got a set!")
                            del player1 [i:i+4]
                            print (player1)
                asking_who = input("Who do you want to ask?:\n")
                while "2" not in asking_who and "3" not in asking_who:
                    print ("Your answer must have either 2 or 3 in it to represent asking Player 2 or Player 3.")
                    asking_who = input("Who do you want to ask?:\n")
                cardnum = input("What card do you want to ask for?:\n")
                while (cardnum != "1" and cardnum != "2" and cardnum != "3" and cardnum != "4" and cardnum != "5" and cardnum != "6" and cardnum != "7" and cardnum != "8" and cardnum != "9" and cardnum != "10" and cardnum != "11" and cardnum != "12" and cardnum != "13" ) or cardnum not in player1:
                    print ("The number has to be within the range of 1 to 13 and must be a card that you have in your hand.")
                    cardnum = input("What card do you want to ask for?:\n")
            else:
                print("Player 2: Go Fish!")
                player1.append(deck_of_cards[0])
                player1 = sorted(player1)
                del deck_of_cards[0]
                if player1[-1] == cardnum: 
                    print("Player 1 got what they asked for from the deck! They get to play again.")
                    current_player = "1"
                    if len(player1) > 3:
                        for i in range(len(player1) - 3):
                            if player1[i] == player1[i + 1] and player1[i] == player1[i + 2] and player1[i] == player1[i + 3]:
                                sets1 += 1
                                print ("You got a set!")
                                del player1 [i:i+4]
                                print (player1)
                    asking_who = input("Who do you want to ask?:\n")
                    while "2" not in asking_who and "3" not in asking_who:
                        print ("Your answer must have either 2 or 3 in it to represent asking Player 2 or Player 3.")
                        asking_who = input("Who do you want to ask?:\n")
                    cardnum = input("What card do you want to ask for?:\n")
                    while (cardnum != "1" and cardnum != "2" and cardnum != "3" and cardnum != "4" and cardnum != "5" and cardnum != "6" and cardnum != "7" and cardnum != "8" and cardnum != "9" and cardnum != "10" and cardnum != "11" and cardnum != "12" and cardnum != "13" ) or cardnum not in player1:
                        print ("The number has to be within the range of 1 to 13 and must be a card that you have in your hand.")
                        cardnum = input("What card do you want to ask for?:\n")
                else:
                    current_player = "2"
        elif "3" in asking_who:
            if cardnum in player3:
                print("Player 3: I have that card.")
                num_of_cards = 0
                i = 0
                while i != len(player3):
                    if player3[i] == cardnum:
                      num_of_cards += 1
                      del player3[i]
                    i += 1
                for i in range (num_of_cards):
                    player1.append(cardnum)
                player1 = sorted(player1)
                print("Player 1: ", player1)
                current_player = "1"
                if len(player1) > 3:
                    for i in range(len(player1) - 3):
                        if player1[i] == player1[i + 1] and player1[i] == player1[i + 2] and player1[i] == player1[i + 3]:
                            sets1 += 1
                            print ("You got a set!")
                            del player1 [i:i+4]
                            print (player1)
                asking_who = input("Who do you want to ask?:\n")
                while "2" not in asking_who and "3" not in asking_who:
                    print ("Your answer must have either 2 or 3 in it to represent asking Player 2 or Player 3.")
                    asking_who = input("Who do you want to ask?:\n")
                cardnum = input("What card do you want to ask for?:\n")
                while (cardnum != "1" and cardnum != "2" and cardnum != "3" and cardnum != "4" and cardnum != "5" and cardnum != "6" and cardnum != "7" and cardnum != "8" and cardnum != "9" and cardnum != "10" and cardnum != "11" and cardnum != "12" and cardnum != "13" ) or cardnum not in player1:
                    print ("The number has to be within the range of 1 to 13 and must be a card that you have in your hand.")
                    cardnum = input("What card do you want to ask for?:\n")
            else:
                print("Player 3: Go Fish!")
                player1.append(deck_of_cards[0])
                player1 = sorted(player1)
                del deck_of_cards[0]
                if player1[-1] == cardnum:
                    print("Player 1 got what they asked for from the deck! They get to play again!")
                    current_player = "1"
                    if len(player1) > 3:
                        for i in range(len(player1) - 3):
                            if player1[i] == player1[i + 1] and player1[i] == player1[i + 2] and player1[i] == player1[i + 3]:
                                sets1 += 1
                                print ("You got a set!")
                                del player1 [i:i+4]
                                print (player1)
                    asking_who = input("Who do you want to ask?:\n")
                    while "2" not in asking_who and "3" not in asking_who:
                        print ("Your answer must have either 2 or 3 in it to represent asking Player 2 or Player 3.")
                        asking_who = input("Who do you want to ask?:\n")
                    cardnum = input("What card do you want to ask for?:\n")
                    while (cardnum != "1" and cardnum != "2" and cardnum != "3" and cardnum != "4" and cardnum != "5" and cardnum != "6" and cardnum != "7" and cardnum != "8" and cardnum != "9" and cardnum != "10" and cardnum != "11" and cardnum != "12" and cardnum != "13" ) or cardnum not in player1:
                        print ("The number has to be within the range of 1 to 13 and must be a card that you have in your hand.")
                        cardnum = input("What card do you want to ask for?:\n")
                else:
                    current_player = "2"
    if len(player2) < 1:
        print ("Player 2 is out of the game.")
        current_player = "3"    
    if current_player == "2" and len(player2) > 0: 
        rand_player2 = ["1", "3"]
        rand_player2 = random.choice(rand_player2) 
        rand_card = random.choice(player2)
        if rand_player2 == "1":
            if rand_card in player1:
                print ("Player 2 asks Player 1 if they have ",rand_card, ". Player 1 has it! ")
                num_of_cards = 0
                i = 0
                while i != len(player1):
                    if player1[i] == cardnum:
                      num_of_cards += 1
                      del player1[i]
                    i += 1
                for i in range (num_of_cards):
                    player2.append(cardnum)
                player2 = sorted(player2)
                print("Player 2: ", player2)
                current_player = "2"
                if len(player2) > 3:
                    for i in range(len(player2) - 3):
                        if player2[i] == player2[i + 1] and player2[i] == player2[i + 2] and player2[i] == player2[i + 3]:
                            sets2 += 1
                            print ("You got a set!")
                            del player2 [i:i+4]
                            print (player2)
            else:
                print ("Player 2 asks Player 1 if they have ",rand_card, ". Player 1 does not have it.")
                player2.append(deck_of_cards[0])
                player2 = sorted(player2)
                del deck_of_cards[0]
                if player2[-1] == rand_card:
                    print("Player 2 got what they asked for from the deck! They get to play again.")
                    current_player = "2"
                    if len(player2) > 3:
                        for i in range(len(player2) - 3):
                            if player2[i] == player2[i + 1] and player2[i] == player2[i + 2] and player2[i] == player2[i + 3]:
                                sets2 += 1
                                print ("You got a set!")
                                del player2 [i:i+4]
                                print (player2)
                else:
                    current_player = "3"
        elif rand_player2 == "3":
            if rand_card in player3:
                print ("Player 2 asks Player 3 if they have ",rand_card, ". Player 3 has it! ")
                num_of_cards = 0
                i = 0
                while i != len(player3):
                    if player3[i] == cardnum:
                      num_of_cards += 1
                      del player3[i]
                    i += 1
                for i in range (num_of_cards):
                    player2.append(cardnum)
                player2 = sorted(player2)
                print("Player 2: ", player2)
                current_player = "2"
                if len(player2) > 3:
                    for i in range(len(player2) - 3):
                        if player2[i] == player2[i + 1] and player2[i] == player2[i + 2] and player2[i] == player2[i + 3]:
                            sets2 += 1
                            print ("You got a set!")
                            del player2 [i:i+4]
                            print (player2)
            else:
                print ("Player 2 asks Player 1 if they have ",rand_card, ". Player 1 does not have it.")
                player2.append(deck_of_cards[0])
                player2 = sorted(player2)
                del deck_of_cards[0]
                if player2[-1] == rand_card:
                    print("Player 2 got what they asked for from the deck! They get to play again.")
                    current_player = "2"
                    if len(player2) > 3:
                        for i in range(len(player2) - 3):
                            if player2[i] == player2[i + 1] and player2[i] == player2[i + 2] and player2[i] == player2[i + 3]:
                                sets2 += 1
                                print ("You got a set!")
                                del player2 [i:i+4]
                                print (player2)
                else:
                    current_player = "3"          
    if len(player3) < 1:
      print ("Player 3 is out of the game.")
      current_player = "1"
    if current_player == "3" and len(player3) > 0:
        rand_player3 = str(randint(1, 2))
        rand_card = random.choice(player3)
        if rand_player3 == "1":
            if rand_card in player1:
                print ("Player 3 asks Player 1 if they have ",rand_card, ". Player 1 has it! ")
                num_of_cards = 0
                i = 0
                while i != len(player1):
                    if player1[i] == cardnum:
                      num_of_cards += 1
                      del player1[i]
                    i += 1
                for i in range (num_of_cards):
                    player3.append(cardnum)
                player3 = sorted(player3)
                print("Player 3: ", player3)
                current_player = "3"
                if len(player3) > 3:
                    for i in range(len(player3) - 3):
                        if player3[i] == player3[i + 1] and player3[i] == player3[i + 2] and player3[i] == player3[i + 3]:
                            sets3 += 1
                            print ("You got a set!")
                            del player3 [i:i+4]
                            print (player3)
            else:
                print ("Player 3 asks Player 1 if they have ",rand_card, ". Player 1 does not have it.")
                player3.append(deck_of_cards[0])
                player3 = sorted(player3)
                del deck_of_cards[0]
                if player3[-1] == rand_card:
                    print("Player 3 got what they asked for from the deck! They get to play again.")
                    current_player = "3"
                    if len(player3) > 3:
                        for i in range(len(player3) - 3):
                            if player3[i] == player3[i + 1] and player3[i] == player3[i + 2] and player3[i] == player3[i + 3]:
                                sets3 += 1
                                print ("You got a set!")
                                del player3 [i:i+4]
                                print (player3)
                else:
                    current_player = "1"
                    asking_who = input("Who do you want to ask?:\n")
                    while "2" not in asking_who and "3" not in asking_who:
                        print ("Your answer must have either 2 or 3 in it to represent asking Player 2 or Player 3.")
                        asking_who = input("Who do you want to ask?:\n")
                    cardnum = input("What card do you want to ask for?:\n")
                    while (cardnum != "1" and cardnum != "2" and cardnum != "3" and cardnum != "4" and cardnum != "5" and cardnum != "6" and cardnum != "7" and cardnum != "8" and cardnum != "9" and cardnum != "10" and cardnum != "11" and cardnum != "12" and cardnum != "13" ) or cardnum not in player1:
                        print ("The number has to be within the range of 1 to 13 and must be a card that you have in your hand.")
                        cardnum = input("What card do you want to ask for?:\n")
        elif rand_player3 == "2":
            if rand_card in player2:
                print ("Player 3 asks Player 2 if they have ",rand_card, ". Player 2 has it! ")
                num_of_cards = 0
                i = 0
                while i != len(player2):
                    if player2[i] == cardnum:
                      num_of_cards += 1
                      del player2[i]
                    i += 1
                for i in range (num_of_cards):
                    player3.append(cardnum)
                player3 = sorted(player3)
                print("Player 3: ", player3)
                current_player = "3"
                if len(player3) > 3:
                    for i in range(len(player3) - 3):
                        if player3[i] == player3[i + 1] and player3[i] == player3[i + 2] and player3[i] == player3[i + 3]:
                            sets3 += 1
                            print ("You got a set!")
                            del player3 [i:i+4]
                            print (player3)
            else:
                print ("Player 3 asks Player 2 if they have ",rand_card, ". Player 2 does not have it.")
                player3.append(deck_of_cards[0])
                player3 = sorted(player3)
                del deck_of_cards[0]
                if player3[-1] == rand_card:
                    print("Player 3 got what they asked for from the deck! They get to play again.")
                    current_player = "3"
                    if len(player3) > 3:
                        for i in range(len(player3) - 3):
                            if player3[i] == player3[i + 1] and player3[i] == player3[i + 2] and player3[i] == player3[i + 3]:
                                sets3 += 1
                                print ("You got a set!")
                                del player3 [i:i+4]
                                print (player3)
                else:
                    current_player = "1"
                    asking_who = input("Who do you want to ask?:\n")
                    while "2" not in asking_who and "3" not in asking_who:
                        print ("Your answer must have either 2 or 3 in it to represent asking Player 2 or Player 3.")
                        asking_who = input("Who do you want to ask?:\n")
                    cardnum = input("What card do you want to ask for?:\n")
                    while (cardnum != "1" and cardnum != "2" and cardnum != "3" and cardnum != "4" and cardnum != "5" and cardnum != "6" and cardnum != "7" and cardnum != "8" and cardnum != "9" and cardnum != "10" and cardnum != "11" and cardnum != "12" and cardnum != "13" ) or cardnum not in player1:
                        print ("The number has to be within the range of 1 to 13 and must be a card that you have in your hand.")
                        cardnum = input("What card do you want to ask for?:\n")
    


print("Game Over!")
print()
time.sleep(2)

if sets1 > sets2 and sets1 > sets3:
  if sets2 > sets3:
    print("Player 1 came first with",sets1,"sets","followed by Player 2 with",sets2,"sets,","and finally Player 3 with",sets3,"sets")
  else:
    print("Player 1 came first with",sets1,"sets","followed by Player 3 with",sets3,"sets,","and finally Player 2 with",sets2,"sets")
if sets2 > sets1 and sets2 > sets3:
  if sets1 > sets3:
    print("Player 2 came first with",sets2,"sets","followed by Player 1 with",sets1,"sets,","and finally Player 3 with",sets3,"sets")
  else:
    print("Player 2 came first with",sets2,"sets","followed by Player 3 with",sets3,"sets,","and finally Player 1 with",sets1,"sets")
if sets3 > sets1 and sets3 > sets2:
  if sets1 > sets2:
    print("Player 3 came first with",sets3,"sets","followed by Player 1 with",sets1,"sets,","and finally Player 2 with",sets2,"sets")
  else:
    print("Player 3 came first with",sets3,"sets","followed by Player 2 with",sets2,"sets,","and finally Player 1 with",sets1,"sets")

if sets1 == sets2 and sets1 == sets3 and sets2 == sets3:
    print("Here are the following scores:")
    print()
    print("Player 1:",sets1,"sets")
    print()
    print("Player 2:",sets2,"sets")
    print()
    print("Player 3:",sets3,"sets")
