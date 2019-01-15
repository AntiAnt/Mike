import random


def d20_roll(adv):
    if adv == 'normal':

        die = random.randint(1,20)

        return die

    if adv == 'advantage':

        die = random.randint(1,20)
        die2 = random.randint(1,20)

     
        if die > die2:
            return die
        if die < die2:
            return die2
        if die == die2:
            return die

    if adv == 'disadvantage':

        die = random.randint(1,20)
        die2 = random.randint(1,20)


        if die > die2:
            return die2
        
        if die < die2:
            return die

        if die == die2:
            return die



print ('normal: ' , d20_roll('normal'))
print ('With disadvantage: ' , d20_roll('disadvantage'))
print ('With advantage: ' , d20_roll('advantage'))