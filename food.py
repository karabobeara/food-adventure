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
