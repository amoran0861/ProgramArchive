#Aidan Moran
#Print rivers and their locations


def RiverList():
    rivers = {
        "USA": "Mississippi River",
        "Brazil": "Amazon River",
        "China": "Yangtze"
        }
    for place in rivers.keys():
        print(rivers[place], "is in", place)
    print("Locations:")
    for place in rivers.keys():
        print(place)
    print("Rivers:")
    for place in rivers.keys():
        print(rivers[place])

def main():
    RiverList()

main()
input("Press enter to exit")
