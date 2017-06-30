<<<<<<< HEAD
import time

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
    else:
        print ("You stayed on the couch for 3 days and starved.")
        replay()

game()
=======



















































# in the kitchen
print ("Do I go to the fridge, freezer, or Costco?")
choice5 = raw_input ()

# picked fridge
if choice5 in ['fridge']:
    print ("You have chosen the fridge.  There are yummy food.")
    time.sleep(2)
    print ("...")
    time.sleep(2)
    print ("walking")
    time.sleep(2)
    print ("... destination reached.")
    time.sleep(1)
    print ("Do you chose the salad or leftovers?")



# picked freezer
if choice5 in ['freezer']:
    print ("You have chosen the colder fridge.  There is ice cream and hot pockets. Well, cold right now.")
    time.sleep(2)
    print ("...")
    time.sleep(2)
    print ("walking")
    time.sleep(2)
    print ("... destination reached.")
    time.sleep(1)
    print ("Do which one do you pick?")

# picked Costco
if choice5 in ['Costco']:
    time.sleep(2)
    print ("...")
    time.sleep(2)
    print ("walking")
    time.sleep(2)
    print ("... destination reached.")
    time(1)
    print ("Lol. Why, there's food in your fridge. What do you want to waste money (protien bars) or save money (free samples)?")
>>>>>>> fb3b6dfdb90bb45e6d0b21c152f0e4c5f1363474
