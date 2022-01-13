from tarotlibrary import cards
import random

##1 select card
##2 check if upright
##3 print meaning
##4 sublementing card
##5 again?

def tarot_round():
    #clear screen
    print(12 * "\n")

    def choosing():
        choice = input("Choose a card between 1 and 4: ")
        choices = ["1","2","3","4"]
        if choice in choices:
                return int(choice)
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

    choice = choosing()

    ##1 select card
    selected = cards[random.randint(0,3)]
    print(selected[0])

    ##2 check if upright
    orientation = upright_check()
    print(str_upright(orientation))

    ##3 print meaning
    print("\nINTERPRETATION\n" + selected[orientation+1])

    ##4 Sublementing card
    sub_orientation = upright_check()
    print("This will be further elaborated by: The " + cards[choice][0] + ", " + str_upright(sub_orientation) + "\n" + cards[choice][sub_orientation+1])

    ##5 again?
    repeat = input("Do you want to get aother reading? (y/n) ")
    if repeat == "y":
        tarot_round()
    else:
        print("OK, bye.")

    

tarot_round()