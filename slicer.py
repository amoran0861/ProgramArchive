#Aidan Moran
#Accept a string and 4 integers. Print string from int 1 to 2, and 3 to 4.

length = 201
theString = ''
while length >= 201:
    theString = input("Please enter a string less than 200 characters long:")
    length = len(theString)

int1 = length+1
while int1 > length:
    int1 = int(input("Please enter integer 1:"))

int2 = length+1
while int2 > length:
    int2 = int(input("Please enter integer 2:"))

int3 = length+1
while int3 > length:
    int3 = int(input("Please enter integer 3:"))

int4 = length+1
while int4 > length:
    int4 = int(input("Please enter integer 4:"))

print(theString[int1:int2])
print(theString[int3:int4])

input("\n\nPress any key to exit")
