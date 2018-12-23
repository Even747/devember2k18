#This is the main executable script for the game

import time
import random
import gmodule

print('Hello!')
print('\n')
#time.sleep(1)

print('Welcome to my test game.')

nimi = input('Name your character: ')
print("Hello {}, hopefully you are ready, because now the fight begins!".format(nimi))

#Script will "roll a dice" here to determine if player wins or loses
num = random.randint(1,6)
#This print is just output what the random number is,
#just to make sure the code works :)
print(num)
#Script for fighting is located in different file, so here we will imput the random number
#to the fight script
gmodule.fight(num)


yesChoice = ['yes', 'y']
noChoice = ['no', 'n']

a = input('Do you want to fight, or not? y/n?').lower()
if a in yesChoice:
        gmodule.fight(num)
elif a in noChoice:
        print('The game ends.' '\n' + 'Bye bye!')
else:
        print ('That is not a valid input')


