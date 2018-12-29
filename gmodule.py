# This is external file for modules and other reusable code
import random
import string


# Method for fight mechanism
from typing import Any, Union


class battle():

    def fight():

        num = random.randint(1, 6)

        # this print output is just to double check the fight method works as intended
        print(num)

        if num >= (5):
            print('You won the fight! Congratulations!')
        else:
            print('You lost the fight :(')
        return

    def rety():

        yesChoice = ['yes', 'y']
        noChoice = ['no', 'n']

        while True:
            print('Would you like to fight again? y/n \n')
            cont = input(''.lower())
            if cont in yesChoice:
                battle.fight()
            elif cont in noChoice:
                break
            else:
                print("Please input either \"yes\" or \"no\".")


def namegen():
    let1 = random.choice(string.ascii_lowercase)
    let2 = random.choice(string.ascii_lowercase)
    let3 = random.choice(string.ascii_lowercase)
    num1 = random.randint(0, 9)
    num2 = random.randint(1000, 9999)
    abc = str(let1) + str(num1) + "-" + str(num2) + str(let2) + str(let3)
    return abc
