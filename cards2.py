#Buld Deck and Get Suit

def build_deck():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + " of " + suit)
    return deck

def get_suit(card):
    currentCard = card.split()
    suit = currentCard[2]
    return suit


#OLD CODE

def randomCardSelect(list):
    cardSelect = []
    cardNumSelected = []
    while len(cardSelect) <= 4:
        range = random.randrange(len(list) - 1)
        if range in cardNumSelected:
            continue
        else:
            cardSelect.append(list[range])
            cardNumSelected.append(range)
    return cardSelect


def menu():
    while True:
        print("\n\n")
        print("Enter a number:")
        print("1. Deal 5 Cards")
        print("2. Quit")
        opt = str(input(">>"))
        if opt == "1":
            print(randomCardSelect(Cards))
        elif opt == "2":
            input("\n\nPress any key to exit.")
            exit()
        else:
            continue
