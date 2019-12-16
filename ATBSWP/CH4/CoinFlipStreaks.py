#Create a program in 2 parts:
#1: Randomly flip a coin 100 times in a row and record the results
#2: Check to see if there are any streaks of 6 or more in the list. Count the number of times it does this.
#3: Do this 10,000 times nad count the total results

import random

numberOfStreaks = 0
hasStreak = 0

for experimentNumber in range(10000):
	coinList = []
	isStreaky = False
	#initialize coin flip list
	for i in range(100):
		if random.randint(0,1) == 0:
			coinList.append('T')
		else:
			coinList.append('H')
	print(coinList)


	for i in range(95):
		if (coinList[i] == coinList[i+1] == coinList[i+2] == coinList[i+3] == coinList[i+4] == coinList[i+5]):
			numberOfStreaks += 1
			isStreaky = True
	if(isStreaky):
		hasStreak += 1


print("Number of Streaks: %s " % numberOfStreaks)
print("Chance of having a streak: %s%%" % (hasStreak/100))
