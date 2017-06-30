import time

=======

#lets go!!!


def replay():
    ask = input("Try again? (yes or no)\n")
    if ask == "yes":
        game()
    else:
        print ("Well fine then....\n")

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
        choice2 = input("Do I go to the fridge, freezer, or Costco?")

            # picked fridge
        if choice2 == "fridge":
            print ("You have chosen the fridge.  There are yummy food.")
            time.sleep(2)
            print ("...")
            time.sleep(2)
            print ("walking")
            time.sleep(2)
            print ("... destination reached.")
            time.sleep(1)
            choice2a = input("Do you chose the salad or leftovers?")

            # pick salad
            if choice2a == "salad":
                print ("Congrats! You're healthy....must be nice...")
                replay()
            # pick leftovers
            if choice2a == "leftovers":
                print ("Did you even check them? No, of course you didn't.... you got dysentary")
                replay()


            # make person pick salad or left overs



            # picked freezer
        if choice2 == "freezer":
            print ("You have chosen the colder fridge.  There are ice cream and hot pockets. Well, cold right now.")
            time.sleep(2)
            print ("...")
            time.sleep(2)
            print ("walking")
            time.sleep(2)
            print ("... destination reached.")
            time.sleep(1)
            choice2b = input("Which on do you pick? (ice cream or hot pocket)")

            #pick ice cream
            if choice2b == "ice cream":
                print ("Now go watch Netflix")
                replay()
            #pick hot pocket
            if choice2b == "hot pocket":
                choice2bi = input("Microwave or thaw?")
                if choice2bi == "microwave"
                    print ("You burn your toungue yet the middle is still freezing...delicious, right?")
                    replay()

                if choice2bi == "thaw"
                    print ("You were starving and gnawed the frozen hunk of cheese and bread... delicious, right?")
                    replay()

            # make them chose one & branch out

            # picked Costco
        if choice2 == "Costco":
            time.sleep(2)
            print ("...")
            time.sleep(2)
            print ("walking")
            time.sleep(2)
            print ("... destination reached.")
            time(1)
            print ("Lol. Why, there's food in your fridge. What do you want to waste money (protien bars) or save money (free samples)?")
            #food pick
    else:
        print ("You stayed on the couch for 3 days and starved.")
        replay()

game()
