#Aidan Moran
#Ask for a tshirt size and message. Print summary. but now with defaults

def SHIRT(size = "Large", message = "I Love Python"):
    print("This is a {} shirt with the message {}".format(size, message))

def main():
    #Book doesn't ask for input
    SHIRT()
    SHIRT(size = "Medium")
    SHIRT("Small", "Hello World")

main()
input("\n\nPress any key to exit.")
