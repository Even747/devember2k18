# This is external file for modules and other reusable code
import random

# Method for fight mechanism
def fight():

    num = random.randint(1, 6)

    #this print output is just to double check the fight method works as intended
    print(num)

    if num >= (5):
        print('You won the fight! Congratulations!')
    else:
        print('You lost the fight :(')
    return

    yesChoice = ['yes', 'y']
    noChoice = ['no', 'n']

    while True:
        # gmodule.fight()
        cont = input('Would you like to fight again? y/n'.lower())
        if cont in yesChoice:
            fight()
        elif cont in noChoice:
            break
        else:
            print('Please input either "yes" or "no".')