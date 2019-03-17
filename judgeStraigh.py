#!/usr/bin/python36

def judgeStraigh(elemlist):
    listofset = set(elemlist)
    if len(listofset) < 5:
        return False
    else:
        translist = elemlist[:]
        if 'J' in translist:
            translist[translist.index('J')] = 11
            print(translist)
        if 'Q' in translist:
            translist[translist.index('Q')] = 12
            print(translist)
        if 'K' in elemlist:
            translist[translist.index('K')] = 13
        if 'A' in translist:
            translist[translist.index('A')] = 14
        sortedlist = sorted(translist)
        #print(sortedlist)
        originlist = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        newStart = originlist.index(sortedlist[0])
        newlist =  originlist[newStart:newStart+5]
        #print(originlist.index(sortedlist[0]))
        #print(newlist)
        #print(translist)
        if sortedlist == newlist:
            return True


if __name__ == '__main__':
    a = [2,5,3,4,6]
    b = [9,7,10,'J',8]
    c = [10,'Q',"K","A",'J']
    d = [2,'Q',"K","A",'J']
    if judgeStraigh(d):
        print('{} is a straigh'.format(d))
    else:
        print('Not a straigh')
        
        
    
        
