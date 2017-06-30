#<<<<<<< HEAD


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
            choice5 = input("Do you chose the salad or leftovers?")

            # make person pick salad or left overs



            # picked freezer
        if choice2 == "freezer":
            print ("You have chosen the colder fridge.  There is ice cream and hot pockets. Well, cold right now.")
            time.sleep(2)
            print ("...")
            time.sleep(2)
            print ("walking")
            time.sleep(2)
            print ("... destination reached.")
            time.sleep(1)
            print ("Do which one do you pick?")

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

#>>>>>>> fb3b6dfdb90bb45e6d0b21c152f0e4c5f1363474
