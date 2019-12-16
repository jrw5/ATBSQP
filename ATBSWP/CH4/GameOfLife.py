#Conway's Game of life from Autmate the Boring Stuff with Python 2nd Edition

import random, time, copy
WIDTH = 60
HEIGHT = 20
i = 0

#Create a list of lists for the cells
nextCells = []
for x in range(WIDTH):
	column = [] #Create a new column
	for y in range(HEIGHT):
		if random.randint(0,1) == 0:
			column.append('#')
		else:
			column.append(' ')
	nextCells.append(column) #NextCells is a list of columns


while True:
	i += 1
	print('\n\n\n\n\n') #Seperate each step with new lines
	currentCells = copy.deepcopy(nextCells)

	for y in range(HEIGHT):
		for x in range(WIDTH):
			print(currentCells[x][y], end='') #print the # or the space
		print() #print a new line at the end of the row.
	for x in range(WIDTH):
		for y in range(HEIGHT):
			#get neighboring coordinates
			#'% WIDTH' ensures left coord is always between 0 and width = -1
			leftCoord = (x - 1) % WIDTH
			rightCoord = (x + 1) % WIDTH
			aboveCoord = (y - 1) % HEIGHT
			belowCoord = (y + 1) % HEIGHT

			#count number of living neighbors
			numNeighbors = 0
			if currentCells[leftCoord][aboveCoord] == '#':
				numNeighbors += 1
			if currentCells[x][aboveCoord] == '#':
				numNeighbors += 1
			if currentCells[rightCoord][aboveCoord] == '#':
				numNeighbors += 1
			if currentCells[leftCoord][y] == '#':
				numNeighbors += 1
			if currentCells[rightCoord][y] == '#':
				numNeighbors += 1
			if currentCells[leftCoord][belowCoord] == '#':
				numNeighbors += 1
			if currentCells[x][belowCoord] == '#':
				numNeighbors += 1
			if currentCells[rightCoord][belowCoord] == '#':
				numNeighbors += 1

			if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
				nextCells[x][y] == '#'
			elif currentCells[x][y] == ' ' and (numNeighbors == 3):
				nextCells[x][y] = '#'
			else:
				nextCells[x][y] = ' '

	time.sleep(1) #Give a one second buffer to prevent flickering
	if i >60:
		break