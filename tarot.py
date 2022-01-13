from tlibclass import deck
import random

##1 select card
##2 check if upright
##3 print meaning
##4 second card
##5 again?

def tarot_round():
    #clear screen
    print(15 * "\n")

    def choosing():
        choices = []
        for c in range(len(deck)):
            choices.append(str(c+1))
            print(str(c+1) + "  ", end="")
        choice = input("\nChoose a card: \n")
        
        if choice in choices:
                return int(choice) - 1
        else:
            print("Wrong input.")
            choosing()

    def upright_check():
        return random.choice([True,False])
    
    # user chooses a card
    choice = choosing()

    ##1 select random card
    selected = deck[random.randint(0,3)]
    # prohibit that the same card shows up twice
    while selected == choice:
        selected = deck[random.randint(0,3)]

    ##2 check if upright
    orientation = upright_check()

    ##3 print meaning
    print(10*"\n" + "YOUR CARDS:\nYour base card is:\n" + selected.give_meaning(orientation))

    ##4 Sublementing card
    sub_orientation = upright_check()
    print("\nThis will be further elaborated by: \n" + deck[choice].give_meaning(sub_orientation))

    ##5 again?
    repeat = input("\n\nDo you want to get another reading? (y/n)\n")
    if repeat == "y":
        tarot_round()
    else:
        print(20*"\n"+"OK, bye.")

tarot_round()