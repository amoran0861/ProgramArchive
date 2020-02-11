#Aidan Moran
#Take 10 inputs from the user and divide them into even, odd, and negetive lists

userNumbers= []
evens= []
odds= []
negetive= []
i = 0
while i < 10:
    i += 1
    integer = int(input('Please enter integer {}:'.format(i)))
    userNumbers.append(integer)
    integer = None

for numb in userNumbers:
    if numb%2 == 0:
        evens.append(numb)
    else:
        odds.append(numb)
    if numb < 0:
        negetive.append(numb)

#0 = even
print("Even numbers:", evens)
print("Odd numbers:", odds)
print("Negetive numbers:", negetive)
input("\n\nPress any key to exit")
