#!/usr/bin/env python3

import random
from collections import deque

def pairup(peopleDict):
    # Takes a list of tuples where 1st element is a name 
    # and 2nd is a list of names that the 1st element can't be paired to
    # Pairs up givers with giftees until a valid list is generated
    
    goodRunFlag = False
    peopleList = list(peopleDict.keys())

    while not goodRunFlag:    
        random.shuffle(peopleList)
        partners = deque(peopleList)
        partners.rotate()
        pairingList = zip(peopleList, partners)
        i = 0
        for pairing in pairingList:
            giver, giftee = pairing
            if giftee in peopleDict[giver]:
                #print('invalid pairing. regenerating')
                goodRunFlag = False
                break
            i=i+1
        
        #print('out of for loop' + str(i))
        if i == (len(partners)):
            goodRunFlag = True
            #for pairing in pairingList:
            #    print(pairing)
        
    return dict(zip(peopleList,partners))

def printpairup(dictPairs):
    # Print results of pairup in a nice way
    for key, value in dictPairs.items():
        print('{0} gives a gift to {1}'.format(key, value))

def main():
    # list of tuples containing a name and forbidden names
    peopleDict = {"Sean": "Nancy,Sarah,Meghan",
                "Nancy": "Sean,Sarah,Meghan",
                "Shannon": "Josh,Heidi",
                "Josh": "Shannon,Heidi",
                "Heidi": "Shannon",
                "Erica": "",
                "Sarah": "Meghan,Sean,Adam,Nancy",
                "Meghan": "Sarah,Sean,Nancy",
                "Colin": "",
                "Adam": "Sarah"}
    pairs = pairup(peopleDict)
    print(pairs)
    printpairup(pairs)

if __name__ == '__main__':
    main()
