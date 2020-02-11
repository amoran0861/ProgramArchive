#Aidan Moran
#Make a guest list then print 3 messages to invite them

# 2 famous people and 1 reletive
guests = ['Tesla', 'Robert DeNitzio', 'Edison']

def main(guestlist):
    for human in guestlist:
        print("hello {} I'm having dinner there will be food and also food please come".format(human))

main(guests)
input("\n\nPress any key to exit")
