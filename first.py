# first, lets say hello

print ("Why hello there, how are you doing?")

# then lets ask some random numer from user

num = input("Could think some number, integer to be precise, and then write it down, please?")

# then the program will cheat and look what the number was and print it out

if num == int:
	print("Was your number", num)
else:
	print("Please try again")	

ans = input("Was I right? y/n")

if ans == "y":
	print("Well, this must be magic :)")
else:
	print("I think someone is lying. That's naughty!")

