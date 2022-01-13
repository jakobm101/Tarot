class Card():
    def __init__(self,number, title, upright_meaning, reversed_meaning):
        self.number = number
        self.title = title
        self.upright_meaning = upright_meaning
        self.reversed_meaning = reversed_meaning

    def give_meaning(self, upright):
        result = "The " + self.title + ", "
        if upright:
            result += "upright: " + self.upright_meaning
        else:
            result += "reversed: " + self.reversed_meaning

        return result

    def __str__(self):
        return (str(self.number) + " " + self.title)

deck = [
    Card(1, "Wizard", "You are magical!",    "You see how things really are."),
    Card(2, "World" , "Assured success, recompense, voyage, route, emigration, flight, change of place.",    "Inertia, fixity, stagnation, permanence."),
    Card(3, "Fool"  , "Folly, mania, extravagance, intoxication, delirium, frenzy, bewrayment.",    "Negligence, absence, distribution, carelessness, apathy, nullity, vanity."),
    Card(4, "Lovers", "Attraction, love, beauty, trials overcome.",    "Failure, foolish designs. Another account speaks of marriage frustrated and contrarieties of all kinds."),
]

### TEST ###
#print(5*"\n" + str(deck[0]) + ", " + str(deck[1]))
#print(deck[0].give_meaning(True))