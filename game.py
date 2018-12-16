#This is the main executable file for the game

import time
import random

print('Hello!')
print('\n')
time.sleep(1)
print('Welcome to my test game.')
name = input('Name your character: ')
print('Hello {}'.format(name),', hopefully you are ready, because now the fight'
                     ' begins!')

#The simple fighting mechanism
#This will simply take random number, and based on that number you either win or lose

for x in range(10):
    print random.randint(1,101)