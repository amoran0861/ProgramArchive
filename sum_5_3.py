#Aidan Moran
#Add all multiples of 5 and 3 under 1000

i = 0
count=0
while i < 1000:
    if i%3 ==0 or i%5 ==0:
        count+=i
    i+=1

#target -  233,168
print(count)
input("\n\nPress any key to exit")
