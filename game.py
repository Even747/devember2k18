#This is the main executable script for the game

import time
import random

print('Hello!')
print('\n')
time.sleep(1)
print('Welcome to my test game.')
name = input('Name your character: ')
print('Hello {}, hopefully you are ready, because now the fight'
                     ' begins!'.format(name))

#The simple fighting mechanism
#This will simply take random number,
#and based on that number you either win or lose
#The idea is to simulate a dice roll

import random
num = random.randint(1,6)

#This print is just output what the random number is,
#just to make sure the code works :)
print(num)

yesChoice = ['yes', 'y']
noChoice = ['no', 'n']



a = input('Do you want to fight, or not? y/n?').lower()
if a in yesChoice:
        if num >= (5):
            print('You won the fight! Congratulations!')
        else:
            print('You lost the fight :(')
elif a in noChoice:
        print('The game ends.' '\n' + 'Bye bye!')


