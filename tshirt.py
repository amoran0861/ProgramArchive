#Aidan Moran
#Ask for a tshirt size and message. Print summary

def SHIRT(size, message):
    print("This is a {} shirt with the message {}".format(size, message))

def main():
    #Book doesn't ask for input
    SHIRT("Small", "Hello World")
    SHIRT(size = "Large", message = "Python")

main()
input("\n\nPress any key to exit.")
