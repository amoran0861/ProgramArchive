#Aidan Moran
#Return a string of city, country

def city_country(city, country):
    #99% chance theres a better way to do this
    return "{}, {}".format(city, country)

def main():
    print(city_country("New York", "USA"))
    print(city_country("Cornwall", "Canada"))
    print(city_country("Naples", "Italy"))

main()
input("\n\nPress any key to exit")
