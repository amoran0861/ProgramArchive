#Aidan Moran
#Write 25 random numbers to a text file

import random

def randwrite():
    textfile = open("random.txt", "w")
    for i in range(24):
        number = random.randint(1,100)
        textfile.write(str(number) + "\n")
    textfile.close()

def main():
    randwrite()

main()
input("Press enter to exit :)")
