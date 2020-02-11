import random

Cards=['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts']
Cards.append('7 of Hearts')
Cards.append('8 of Hearts')
Cards.append('9 of Hearts')
Cards.append('10 of Hearts')
Cards.insert(0, 'Ace of Hearts')
Cards.append('Jack of Hearts')
Cards.insert(11,'Queen of Hearts')
Cards.insert(12,'King of Hearts')


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

def main():
    menu()

main()
