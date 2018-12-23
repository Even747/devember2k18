#This is the main executable script for the game

import time
import gmodule

print('Hello!')
print('\n')
#time.sleep(1)

print('Welcome to my test game.')

nimi = input('Name your character: ')
print("Hello {}, hopefully you are ready, because now the fight begins!".format(nimi))
time.sleep(1)

#Script for fighting is located in different file
#First the fighting method is used once,
#and after that player is asked if he want's to fight again

gmodule.fight()

'''
yesChoice = ['yes', 'y']
noChoice = ['no', 'n']

while True:
        #gmodule.fight()
        cont = input('Would you like to fight again? y/n'.lower())
        if cont in yesChoice:
                gmodule.fight()
        elif cont in (noChoice):
                break
        else:
                print('Please input either "yes" or "no".')
'''


