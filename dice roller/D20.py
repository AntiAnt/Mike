import random

die = random.randint(1,20)


def atkroll(num_die,Adv):
    if num_die == 1:
        return print ('Rolled',die)
    if num_die == 2:
        return print ('Rolled',die,die)
atkroll(1,0)
atkroll(2,0)