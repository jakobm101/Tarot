from tarotlibrary import cards
from tlibclass import deck
import random

# test
#print(deck[1].give_meaning(True))

##1 select card
##2 check if upright
##3 print meaning
##4 sublementing card
##5 again?

def tarot_round():
    #clear screen
    print(15 * "\n")

    def choosing():
        choice = input("Choose a card between 1 and 4: ")
        choices = ["1","2","3","4"]
        if choice in choices:
                return int(choice) - 1
        else:
            print("Wrong input.")
            choosing()

    def upright_check():
        return random.choice([True,False])

    def str_upright(bool):
        if bool:
            return ("reversed")
        else:
            return ("upright")
    
    # choose a card
    choice = choosing()

    ##1 select card
    selected = deck[random.randint(0,3)]
    # prohibit that the same card show up twice
    while selected == choice:
        selected = deck[random.randint(0,3)]

    print(10*"\n" + "YOUR CARDS:\nThe " + selected[0], end=", ")

    ##2 check if upright
    orientation = upright_check()
    print(str_upright(orientation))

    ##3 print meaning
    print("\nINTERPRETATION\n" + selected[orientation+1])

    ##4 Sublementing card
    sub_orientation = upright_check()
    print("\nThis will be further elaborated by: \nThe " + cards[choice][0] + ", " + str_upright(sub_orientation) + "\n" + cards[choice][sub_orientation+1])

    ##5 again?
    repeat = input("Do you want to get another reading? (y/n) ")
    if repeat == "y":
        tarot_round()
    else:
        print(20*"\n"+"OK, bye.")

tarot_round()