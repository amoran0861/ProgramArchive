#Aidan Moran
#Make a guest list then print 3 messages to invite them

def invite(guestlist):
    for human in guestlist:
        print("hello {} I'm having dinner there will be food and also food please come".format(human))

def main():
    # 2 famous people and 1 reletive
    guests = ['Tesla', 'Robert DeNitzio', 'Edison']
    invite(guests)
    print('We have a bigger table bring a +1')
    guests.insert(0, 'Bill Nye The Science Guy')
    guests.insert(2, 'An Alien')
    guests.append('Cave Johnson')
    invite(guests)

main()
input("\n\nPress any key to exit")
