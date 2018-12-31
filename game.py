# This is the main executable script for the game

import time
import gmodule

# Purpose for this "namegen" will be revealed later. :)
aname = gmodule.namegen()

# Title menu

gmodule.tmenu.menu()


print('Hello!')
print('\n')
#time.sleep(1)

print('Welcome to my test game.')

nimi = input('Name your character: ')
print("Hello {}, hopefully you are ready, "
      "because now the fight begins!".format(nimi))
time.sleep(1)

# Script for fighting is located in different file
# First the fighting method is used once,
# and after that player is asked if he want's to fight again

gmodule.battle.fight()
gmodule.battle.rety()

bye1 = 'Thank you for playing! \n'
bye2 = 'The game will now exit.'

print(bye1 + bye2)