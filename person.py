#Aidan Moran
#Make a dictionary about a person and store information

def makeProfileDict():
    txtfile = open("person.txt", "r")
    txtfile = txtfile.readlines()
    person = {
        "first_name": txtfile[0].replace("\n",""),
        "last_name": txtfile[1].replace("\n",""),
        "age": txtfile[2].replace("\n",""),
        "city": txtfile[3].replace("\n",""),
    }
    return person

def main():
    person = makeProfileDict()
    print("First Name is", person['first_name'])
    print("Last Name is", person['last_name'])
    print("Age is", person['age'])
    print("They live in", person['city'])


main()
input("Press enter to exit")
