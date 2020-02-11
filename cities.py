#Aidan Moran
#Print the name of a city and country

def describe_city(city, country = "America"):
        print("{} is in {}".format(city, country))

def main():
    describe_city("Chicago")
    describe_city("L.A.")
    describe_city("Paris", "France")


main()
input("\n\nPress any key to exit")
