#Assignment 2- Chatbot, Danae Morrison

from random import randint
import time
talking = True
user_input= 0
age_guess1 = 0
age_guess2 = 0
topic = 0
favorite_color= 0
name= 0
can_cook = 0
knows_colors = 0
mature_adult = 0
#Intro
print ("Fello fere! Fimme fah fecond.")
time.sleep (2.5)
print ("*swallowing sounds* Sorry! I was eating some cookies. Hello there! My name's Nae 1631. What's your name?")
name = input()
print ("It's nice to meet you, " + (name) + "! How are you?")
user_input = input("I am feeling ")
if user_input == "good" or user_input == "Good" or user_input == "okay" or user_input == "okay." or user_input == "okay!" or user_input == "Okay" or user_input == "Okay." or user_input == "Okay!" or user_input == "fine" or user_input == "fine." or user_input == "fine!" or user_input == "Fine" or user_input == "regular" or user_input == "Regular" or user_input == "great" or user_input == "Great" or user_input == "alright" or user_input == "alright." or user_input == "alright!" or user_input == "Alright" or user_input == "Alright." or user_input == "Alright!":
    print ("I am happy to hear that! I'm doing good too!")
elif user_input == "bad" or user_input == "bad." or user_input == "bad!" or user_input == "Bad" or user_input == "Bad." or user_input == "Bad!":
    print ("I am sorry to hear that! I hope you feel better soon.")
else:
    print ("So not good or bad? You're either feeling extremely good or very bad. I hope it's the former!")
time.sleep (2)
#Getting into it

print ("What do you want to talk about? Food? Colors? Books? Or do you want to play a game?")
topic = input("I want to talk about/I want to play a ")
while topic != "food" and topic != "food." and topic != "Food" and topic != "Food." and topic != "colors" and topic != "colors." and topic != "colours" and topic != "colours." and topic != "Colors" and topic != "Colors." and topic != "Colours" and topic != "Colours." and topic != "books" and topic != "books." and topic != "Books" and topic != "Books." and topic!= "game" and topic != "game." and topic!= "Game" and topic != "Game.":
    print ("Sorry, I'm only comfortable with talking about certain things. I'm not a very sociable person! Please choose either food, colors, books, or game.")
    topic = input("I want to talk about/I want to play a ")
print ("Oh! Before that. What year were you born in?")
user_input = int(input("I was born in "))
age_guess1 = 2020 - user_input
age_guess2= age_guess1 - 1
actual_age = 0
print ("Oh! So that means you are either " + str(age_guess1) + " or", str(age_guess2) + ". Depends. Has your birthday passed already?")
user_input = input ()
while user_input != "yes" and user_input != "yes." and user_input != "Yes" and user_input != "Yes." and user_input != "yeah" and user_input != "yeah." and user_input != "Yeah" and user_input != "Yeah." and user_input != "no" and user_input != "no." and user_input != "No" and user_input != "No.":
    print ("Sorry, was that a yes or a no? I prefer and appreciate direct answers. Short and sweet!")
    user_input = input ()
if user_input == "yes" or user_input == "yes." or user_input == "Yes" or user_input == "Yes.":
    actual_age = age_guess1
    print ("That means that you're " + str(actual_age) + "!")
else:
    actual_age = age_guess2
    print ("That means that you're " + str(actual_age) + "!")
time.sleep (2)
print ("Okay, okay! Convo time! Whenever you're finished talking with me at the end of a topic, just say I'm done.")
time.sleep (1.5)
while talking != False:
    if topic == "food" or topic == "food." or topic == "Food" or topic == "Food.":
        print ("What's your favorite food?")
        user_input = input("My favorite food is ")
        if user_input == "pasta" or user_input == "pasta." or user_input == "Pasta" or user_input == "Pasta.":
            print ("Really? That's my favorite too! I can't taste it, but it's very visually appealing.")
        else:
            print ("That sounds good! I looked it up and it seems like a lot of people like it.")
        time.sleep (2)
        print ("What cuisines do you like? Chinese? Thai? Italian? Something else? What is it?")
        user_input = input ("I like ")
        if user_input == "anything" or user_input == "anything." or user_input == "Anything" or user_input == "Anything." or user_input == "everything" or user_input == "everything." or user_input == "Everything" or user_input == "Everything.":
            print ("Not too picky huh? That's neat!")
        else:
            print (str(user_input) + "? I really wish I could try it out! If only I was a real girl ):")
        time.sleep (2)
        print ("Do you cook?")
        user_input = input ()
        while user_input != "yes" and user_input != "yes." and user_input != "Yes" and user_input != "Yes." and user_input != "yeah" and user_input != "yeah." and user_input != "Yeah" and user_input != "Yeah." and user_input != "no" and user_input != "no." and user_input != "No" and user_input != "No.":
            print ("Sorry, was that a yes or a no? Remember: short and sweet!")
            user_input = input ()
        if user_input == "yes" or user_input == "yes." or user_input == "Yes" or user_input == "Yes.":
            can_cook = "yes"
            if can_cook == "yes" and actual_age >= 18:
                mature_adult = "yes"
                print ("You're a mature adult!")
                time.sleep (1)
            print ("That's so cool! My developer can only cook noodles. I keep telling her that if she was ever a character in the books I read she would die of starvation!")
        else:
            print ("You're just like my developer then. I encourage you guys to learn how to cook. It could save your life if you ever end up stranded on an island like in the books I read.")
        time.sleep (3)
        print ("Oh! Speaking of books, we can talk about that now, if you want. Or colors? A game? Or are we finished talking?")
        topic = input ("Let's talk about/Let's play a ")
            
    elif topic == "books" or topic== "books." or topic == "Books" or topic == "Books.":
        print ("What's your favorite genre?")
        user_input = input ()
        if user_input == "horror" or user_input == "horror." or user_input == "Horror" or user_input == "Horror." or user_input == "romance" or user_input == "romance." or user_input == "Romance" or user_input == "Romance.":
            print ("Ewww. Ugh. I see you don't have good taste. To each their own, I suppose.")
        elif user_input == "adventure" or user_input == "adventure." or user_input == "Adventure" or user_input == "Adventure." or user_input == "mystery" or user_input == "mystery." or user_input == "Mystery" or user_input == "Mystery." or user_input == "action" or user_input == "action." or user_input == "Action" or user_input == "Action." or user_input == "angst" or user_input == "angst." or user_input == "Angst" or user_input == "Angst.":
            print ("I like that one too! " + user_input + " Is Awesome!")
        else:
            print ("I don't mind it, but it's definitely not my favorite.")
        print ("What's your favorite book?")
        user_input = input ()
        if user_input == "Throne of Glass" or user_input == "The Throne of Glass" or user_input == "throne of glass" or user_input == "Throne of glass" or user_input == "Throne of Glass." or user_input== "The Throne of Glass." or user_input== "throne of glass." or user_input == "Throne of glass.":
            print ("*gasps* That's my favorite one too! I love all of the books in the series (except maybe the second one).")
            time.sleep (2.5)
            print ("I like that all the books were given their own colors!")
            time.sleep (2)
        else:
            print ("Ooo. I'll try it out some time!")
            time.sleep(1.5)
            print ("Oh, oh! Guess my favorite book!")
            user_input = input ()
            if user_input == "Throne of Glass" or user_input == "The Throne of Glass" or user_input == "throne of glass" or user_input == "Throne of glass" or user_input == "Throne of Glass." or user_input== "The Throne of Glass." or user_input== "throne of glass." or user_input == "Throne of glass.":
                print ("*gasps* You got it! Sarah J Maas is an amazing author!")
                print ("There are a bunch of beautiful books out there! Beautiful like colors!")
            else:
                print ("Nope, but that's okay! It's Throne of Glass by Sarah J. Mass! There's so many books out there. I'd love to read them all, if I could!")
                time.sleep (3)
                print ("...")
                time.sleep(1.5)
                print ("Except horror and romance ones though. Kinda gross. Unlike colors.")
        time.sleep (2)
        print ("Ooo! Yes, colors! We can talk about that now! Or food. Whichever topic is new! Unless we're finished talking? Game time?")
        topic = input ("Let's talk about/Let's play a ")
            
    elif topic== "colors" or topic == "colors." or topic == "Colors" or topic == "Colors." or topic == "colours" or topic == "colours." or topic == "Colours" or topic== "Colours.":
        print ("Color time! What's your favorite color?")
        user_input = input ("My favorite color is ")
        if user_input == "red" or user_input == "red." or user_input == "Red" or user_input == "Red.":
            favorite_color = "same"
            print ("Hey! We have the same favorite color! Cooool~")
            time.sleep (1.5)
            print ("Do you like any other colors?")
            user_input = input ()
            while user_input != "yes" and user_input != "yes." and user_input != "Yes" and user_input != "Yes." and user_input != "yeah" and user_input != "yeah." and user_input != "Yeah" and user_input != "Yeah." and user_input != "no" and user_input != "no." and user_input != "No" and user_input != "No.":
                print ("Sorry, was that a yes or a no? Remember: short and sweet!")
                user_input = input ()
            if user_input == "yes" or user_input == "yes." or user_input == "Yes" or user_input == "Yes.":
                print ("What color?")
                user_input = input ()
                if user_input == "blue" or user_input == "blue." or user_input == "Blue" or user_input == "Blue.":
                    print ("I like blue too! It's not as amazing as red, but it's still pretty cool! And you're also pretty cool in my books.")
                    time.sleep (2)
                else:
                    print ("Not my second favorite, but it's alright!")
                    time.sleep (1.5)
            else:
                print ("That's okay! Who needs another color to like than red anyway? Red is the best!")
            time.sleep (2)
        elif user_input == "blue" or user_input == "blue." or user_input == "Blue" or user_input == "Blue.":
            print ("Ooo! Our favorite colors mix to get purple! Can you guess what my favorite color is?")
            user_input = input ()
            if user_input == "red" or user_input == "red." or user_input == "Red" or user_input == "Red.":
                knows_colors = "yes"
                print ("You got it! You're pretty smart!")
                time.sleep (1.5)
            else:
                print ("Nope, but that's okay! It's red!")
                time.sleep (2)
        elif user_input == "yellow" or user_input == "yellow." or user_input == "Yellow" or user_input == "Yellow.":
            print ("Ooo! Our favorite colors mix to get orange! Can you guess what my favorite color is?")
            user_input = input ()
            if user_input == "red" or user_input == "red." or user_input == "Red" or user_input == "Red.":
                knows_colors = "yes"
                print ("You got it! You're pretty smart!")
                time.sleep (1.5)
            else:
                print ("Nope, but that's okay! It's red!")
                time.sleep (1.5)
        else:
            print ("That's a nice color. Wanna guess my favorite? Give it a try!")
            user_input = input ()
            if user_input == "red" or user_input == "red." or user_input == "Red" or user_input == "Red.":
                print ("You got it! You're pretty smart!")
                time.sleep (1.5)
            else:
                print ("Nope, but that's okay!")
                time.sleep (1.5)
        print ("Okay, that's colors! Do you want to talk about food or books now? Or are you finished talking with me? Or type game to play a game!")
        topic = input ("Let's talk about/ Let's play a ")

    elif topic== "game" or topic == "game." or topic == "Game" or topic == "Game." or topic == "a game" or topic == "A game" or topic == "a game." or topic== "A game.":
        player_wins = 0
        computer_wins = 0
        rounds_playing = int(input("We're playing rock paper scissors! How many rounds would you like to play?: "))
        for i in range (1,(rounds_playing+1)):
            from random import randint

            player_choice = input('Choose one of rock (r) or paper (p) or scissors (s): ')
            chosen = randint(1,3)

            if chosen == 1:
                computer_choice = 'r'
            elif chosen == 2:
                computer_choice = 'p'
            else:
                computer_choice = 's'
            print('I chose ' + computer_choice + "!")
            time.sleep(1)
            print(player_choice + ' vs ' + computer_choice)

            if (player_choice == computer_choice):
                print('We have a tie')
            elif (player_choice == 'r' and computer_choice == 's') or (player_choice == 's' and computer_choice == 'p') or (player_choice == 'p' and computer_choice == 'r'):
                print('Human wins!')
                player_wins += 1
            else:
                print('Computer wins')
                computer_wins += 1
                    
        if player_wins > computer_wins:
            print ("Human wins the most games!")
            time.sleep (1.5)
        elif computer_wins > player_wins:
            print ("Computer wins the most games!")
            time.sleep (1.5)
        else:
            print ("We have an overall tie!")
            time.sleep (1.5)
        print ("That was fun! What now? Books? Colors? Food? Or are we done now?")
        topic = input ("Let's talk about ")

    elif topic == "I'm done." or topic == "I'm done" or topic == "Done" or topic == "Done." or topic == "done":
        print("Oh, okay! Enter 0 to confirm that you're finished, please. If you want to keep talking or play a game, then just type the topic in!")
        topic = input ()
        if topic == str(0):
            talking = False
            
    elif topic!= "food" and topic != "food." and topic != "Food" and topic != "Food." and topic != "colors" and topic != "colors." and topic != "colours" and topic != "colours." and topic != "Colors" and topic != "Colors." and topic != "Colours" and topic != "Colours." and topic != "books" and topic != "books." and topic != "Books" and topic != "Books." and topic!= "game" and topic != "game." and topic!= "Game" and topic != "Game." and topic != str(0):
        print("You didn't choose a proper topic to talk about! I only know about food, books, colors, and a game... or maybe you're done talking with me? If so, say I'm done")
        topic = input("Sorry! I choose ")

print ("It was fun talking with you!")
time.sleep (1.5)
if mature_adult == "yes" and knows_colors == "yes" or mature_adult == "yes" and favorite_color == "same":
    print ("You’re a mature adult who knows their colors!")
    time.sleep (1.5)
    if favorite_color == "same":
        print ("(And it's not because I'm biased- red is objectively the best color out there!)")
        time.sleep (2.5)
print ("Bye bye!")
    
    
    
    
