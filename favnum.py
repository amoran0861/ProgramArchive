#Aidan Moran
#Dictionary of favorite numbers

theBestNumbers = {
    "Kevin": "1",
    "Kevin 2": "2",
    "Steven": "83",
    "Not Kevin": "-1",
    "Chloe": "41"
}

def addNumbers(numberList):
    adding = True
    while adding == True:
        print("To add a value, type \"Name\" - \"Number\", to quit, type \"quit\"")
        numberAdd = input(">>")
        numberAdd = str(numberAdd)
        numberAdd = numberAdd.replace(" ","")
        if numberAdd == "quit":
            adding = False
        else:
            numberAdd = numberAdd.split("-")
            numberList[numberAdd[0]] = numberAdd[1]
    return numberList

def main(theBestNumbers):
    numberDict = addNumbers(theBestNumbers)
    print(numberDict)

main(theBestNumbers)
input("Press enter to exit")
