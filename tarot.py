from tarotlibrary import cards
import random

##1 select card
##2 check if upright
##3 print meaning

#clear screen
print(12*"\n")

##1 select card
print(cards[random.randint(0,3)][0])

##2 check if upright
reversed = random.choice([True,False])
if reversed:
    print("reversed")
else:
    print("upright")

##3 print meaning
print(2*"\n"+"")