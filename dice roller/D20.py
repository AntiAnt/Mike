import random



def atkroll(num_die,Adv):
    if num_die == 1:

        die = random.randint(1,20)

        return die

    if num_die == 2:

        die = random.randint(1,20)
        die2 = random.randint(1,20)

        return die , die2

    if num_die == 3:

        die = random.randint(1,20)
        die2 = random.randint(1,20)
        die3 = random.randint(1,20)

        return die , die2 , die3

print ('rolled' , atkroll(1,0))
print ('rolled' , atkroll(2,0))
print ('rolled' , atkroll(3,0))

#def adv(roll_with_adv):
    #while roll_with_adv == 