import time

#lets go!!!

def replay():
    ask = input("Try again? (yes or no)\n")
    if ask == "yes":
        game()
    else:
        print ("Well fine then....you suck.\n")

def game():

    print ("I'm hungry teen - home alone but very lazy\n")
    #sleep(3)
    couch = input("Get off the couch? (yes or no)\n")
    if couch == "yes":
#tab here

        print ("* walk to kitchen *")
        time.sleep(1)
#start 2nd path
            # in the kitchen
        choice2 = input("Do I go to the fridge, freezer, or costco?\n")

            # picked fridge
        if choice2 == "fridge":
            print ("You have chosen the fridge.  There is yummy food.")
            time.sleep(1)
            print ("...")
            time.sleep(1)
            print ("walking")
            time.sleep(1)
            print ("... destination reached.\n")
            time.sleep(1)
            choice2a = input("Do you chose the salad, chicken, or leftovers?")

            # pick salad
            if choice2a == "salad":
                print ("Congrats! You're healthy...\n")
                time.sleep(1)
                print ("for once...\nmust be nice...")
                time.sleep(1)
<<<<<<< HEAD
                print ("lol. you win at life. jk only this game.\n")
=======
                print ("lol. You win at life. jk only this game.\n")
>>>>>>> cd09237df66fca35387c7c37b4b44a247660d215
                replay()
            # pick leftovers
            if choice2a == "leftovers":
                print ("Did you even check them? No, of course you didn't...you got dysentary\n")
                replay()

            if choice2a == "chicken":
                choice2ai = input("What's your favorite type of chicken?\nfried or grilled?\n")
                if choice2ai == "fried"
                    print ("You enjoy a delicious and quick meal\n")
                    replay()
                if choice2ai == "grilled"
                    print("Your cooking skills are next level!! You rock and eat well for the next week!")
                    replay()
        if choice2 == "freezer":
            print ("You have chosen the colder fridge.\nThere are ice cream and hot pockets. Well, cold right now.")
            time.sleep(2)
            print ("...")
            time.sleep(1)
            print ("* walking *")
            time.sleep(1)
            print ("... destination reached.\n")
            time.sleep(1)
            choice2b = input("Which do you pick? (ice cream or hot pocket)\n")

            #pick ice cream
            if choice2b == "ice cream":
                print ("Now go watch Netflix.\n")
                time.sleep(2)
<<<<<<< HEAD
                print ("...You're now a professional procrastinator. LOL.\nNow get your butt of the couch and try again.\n")
=======
                print ("...You're now a professonal procrastinator. LOL.\nNow get your butt off the couch and try again.\n")
>>>>>>> cd09237df66fca35387c7c37b4b44a247660d215
                replay()
            #pick hot pocket
            if choice2b == "hot pocket":
                choice2bi = input("Microwave or thaw?\n")
                if choice2bi == "microwave":
                    print ("You burn your toungue yet the middle is still freezing...delicious, right?\nYou rush to the ER due to excessive heartburn...\n")
                    time.sleep(3)
<<<<<<< HEAD
                    print ("The anticipation is killing me...no wait...it's killing you.\n")
                    time.sleep(2)
                    print ("You died. LOL.\n")
=======
                    print ("The anticipation is killing me...no wait it's killing you.\n")
                    time.sleep(2)
                    print("You died. LOL.\n")
>>>>>>> cd09237df66fca35387c7c37b4b44a247660d215
                    replay()

                if choice2bi == "thaw":
                    print ("You were starving and gnawed the frozen hunk of cheese and bread\n...you chipped a molar\n...delicious, right?\n")
                    replay()

            # picked Costco
        if choice2 == "costco":
            time.sleep(1)
            print ("...")
            time.sleep(1)
            print ("walking")
            time.sleep(1)
            print ("... destination reached.\n")
            time.sleep(1)
            print ("Lol. Why, there's food in your fridge.\n")

            choice2c = input("Do you want to waste money (protein bars)? Save money (free samples)?\n")
            if choice2c == "protein bars":
                print ("Now you have less money and have to workout :(\n")
                time.sleep(2)
<<<<<<< HEAD
                print ("You go home...\n")
                time.sleep(2)
                print ("You attempt to do a push-up\n...you break both arms. LOL.\n")
                replay()

            if choice2c == "free samples":
                print ("Yay free food! You must budget...noice.\n")
                time.sleep(1)
                print ("3 years later...\n")
                time.sleep(3)
                print ("You have saved up enough for a mansion. LIT.\n")
                time.sleep(3)
                print ("But you're alone. LOL.\n")
                replay()

=======
                print("You go home...\n")
                time.sleep(2)
                print ("You attempt to do a push-up\n...you break both arms. LOL.\n")
                replay()
>>>>>>> cd09237df66fca35387c7c37b4b44a247660d215

            if choice2c == "free samples":
                print ("Yay free food! You must budget...noice.\n")
                time.sleep(1)
                print ("3 years later...\n")
                time.sleep(3)
                print ("You have saved enough for a mansion. LIT.\n")
                time.sleep(3)
                print ("But you're alone. LOL.\n")
                replay()







#first ending
    else:
        print ("You stayed on the couch for 3 days and starved to death. LOL.\n")
        replay()

game()
