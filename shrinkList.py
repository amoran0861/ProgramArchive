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
    print('ok we have some budget cuts and can only invite 2 of you')
    for i in range(4):
        leave = guests[0]
        print('Bye, {}'.format(leave))
        guests.pop(0)
    invite(guests)
    #remove the rest
    del guests[0]
    del guests[0]
    print(guests)

main()
input("\n\nPress any key to exit")
