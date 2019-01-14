name = input('What Shall We put on your Tombstone?:')

import random

print ('hello' , name)

gold_loc = [(1,1) , (-1,4) , (-1,-2)]

gold = 0
x = 0
y = 0

while True:
    walk = input('Which way: ' + name + '?')
    if walk == 'e' or walk == 'east':
        x = x + 1
        print (name, 'walks east')
    if walk == 'w' or walk == 'west':
        x = x - 1
        print (name, 'walks west')
    if walk == 'n' or walk == 'north':
        y += 1
        print (name, 'walks north')
    if walk in ('s' , 'south'):
        y -= 1
        print (name, 'walks south')
    if (x , y) in gold_loc:
        gold += random.randint(1,20) 
        print ('you find ten gold on the corpse of a poor soul')
        gold_loc.remove ((x , y))

    if walk in ('q' , 'quit'):
        print ('goodbye')
        break
        
    print (x , ',' , y)
    print (gold)
    print (len(gold_loc) , 'Members still lost' )