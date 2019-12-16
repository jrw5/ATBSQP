# Collatz sequence program
#Joel Wheatley
#12/6/19

import sys

def collatz(num):
	if((num%2)==0):
		return int(num/2)
	else:
		return int(num*3+1)


print("What number do you want to put into the Collatz Sequence?")
try:
	num = int(input())
except ValueError:
	print("Please insert an Integer")
	sys.exit()


try:
	while(num != 1):
		num = collatz(num)
		print(num)
except KeyboardInterrupt:
	sys.exit()
