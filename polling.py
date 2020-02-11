#Aidan Moran
#See of someone took a pole, or else invite them to take it


def poll():
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
    nameIn = input("What is your name?: ")
    if nameIn in favorite_languages:
        print("Your favorite language is {}".format(favorite_languages[nameIn]))
    else:
        print("Your name isn't in the poll. What\'s your favorite language?")
        language = input(">>")
        favorite_languages[nameIn] = language

def main():
    poll()
    input("press enter to exit")


main()
