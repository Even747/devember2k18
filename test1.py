# Don't mind this file, this is just for testing and playing around
# Code in here might or might not work, and could potentially be hazardous to mental health.
# Viewer discretion is advised.

'''

Put some stuff in comments to avoid printing out all the unnecessary stuff.

counter = 100
miles = 1000.0
name = "John"

print ("This is some random number: ", counter)
print ("These are the miles", name, "has travelled", miles)
print ("Name of the brave traveller: ", name)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
list3 = ['a','b','c'];
list4 = ['Berlin', 'Tokyo', 'Sofia', 'Helsinki', 'Paris', 'Canberra'];
list5 = ['Foo', 'Blaa', 42, 747, 'idk wtf'];

print (list4[0:5])
print (list2[1:10])
#print (list5[1,3,5]) find out how to access only certain list entries
'''

'''
import time
import calendar

print (time.localtime());

cal = calendar.month(2018, 12)
print ("Here is the calendar:")
print (cal)
'''

'''
def print_func( par ):
    print ("Hello: ", par)
    return

print_func("Mary")
print_func("James")
print_func("Liz")
print("\n")
'''
import moduletest

'''
moduletest.xyz("Jee Jee")
print("\n")
moduletest.math(1,2)
print("\n")

cat = moduletest.Animal('Rollo', 33)

print(cat.get_name(),cat.get_height())
print(cat.abc())

p1 = moduletest.Person('Mike', 42)

print("Developer name is: ", p1.name,',and age is: ',p1.age)
'''

#file I/O testing
'''
file1 = open("test.txt", "wb")

file1.write(bytes("Write this text to the test file\n", "UTF-8"))
file1.write(bytes("Write this too to the test file: LOL this works?","UTF-8"))

file1.close()
'''
'''
file1 = open("test.txt", "r+")
file2 = open('readtest.txt', 'r+')

read_text = file1.read()
print(read_text)

print('\n')

read_text = file2.read()
print(read_text)
'''

'''
# just testing functions
def printme(str, str2):
    print(str, str2)
    print(str)
    print(str2)
    return

printme('Hi!', 'Hi again!')

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return

# Now you can call sum function
total = sum( 10, 20 )
print ("Outside the function : ", total )

print('\n')

x = input('something:')
print(x)
'''





'''
import random
num = random.randint(1,10)
print(num)
'''
'''
name = ('James')
print('Hello {}, how are you doing?'.format(name))
print('Hello', name + ', how are you doing?')
'''

import gmodule

gmodule.fight()




































