#Aidan Moran
#Take an input text file of water usage and output weeks it will last

import math

def hydrateOrDiedrate():
    textfile = open("water.txt", "r")
    writefile = open("usage.txt", "w")
    usage = textfile.readlines()
    for gallons in usage:
        gallons = int(gallons)
        if gallons == 0:
            writefile.write("This water will last forever!\n")
        else:
            weeksleft = math.floor(10000 / gallons)
            writefile.write("This water will last {} week(s)\n".format(weeksleft))
    textfile.close()
    writefile.close()

def main():
    hydrateOrDiedrate()

main()
input("Press Enter To Exit")
