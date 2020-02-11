#Aidan Moran
#Find info on a text file

def linecount():
    textfile = open("programs3.txt", "r")
    txtlc = textfile.readlines()
    #print(txtlc)
    textlength = len(txtlc)
    textfile.close()
    return textlength

def wordcount():
    textfile = open("programs3.txt", "r")
    words = linecount()
    txtwc = textfile.read()
    #print(txtwc)
    for char in txtwc:
        if char == " ":
            words += 1
    textfile.close()
    return words

def fourletter():
    textfile = open("programs3.txt", "r")
    txt4l = textfile.read().replace("\n"," ")
    txt4list = txt4l.split(" ")
    fourwords = 0
    for word in txt4list:
        if len(word) == 4:
            fourwords += 1
    textfile.close()
    return fourwords

def vowels():
    textfile = open("programs3.txt", "r")
    txtv = textfile.read()
    txtv = list(txtv)
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for char in txtv:
        if char == "a":
            a += 1
        if char == "e":
            e += 1
        if char == "i":
            i += 1
        if char == "o":
            o += 1
        if char == "u":
            u += 1
    textfile.close()
    finalv = "{} A, {} E, {} I, {} O, {} U".format(a,e,i,o,u)
    return finalv

def longest():
    textfile = open("programs3.txt", "r")
    txtlong = textfile.read()
    txtlong = txtlong.replace("\n"," ")
    txtlong = txtlong.split(" ")
    longestword = "a"
    for word in txtlong:
        if len(word) > len(longestword):
            longestword = word
    textfile.close()
    return longestword

def main():
    print("Lines: {}".format(linecount()))
    print("Words: {}".format(wordcount()))
    print("4 Letter Words: {}".format(fourletter()))
    print("Vowels: {}".format(vowels()))
    print("Longest Word: {}".format(longest()))

main()
input("Press enter to exit")
