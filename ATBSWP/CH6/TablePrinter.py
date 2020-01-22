#Table Printer
#Joel Wheatley
#1/21/20


tableData = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
	widthArray = []
	k=0
	for i in range(len(table)):
		if k < len(table[i]):
			k = len(table[i])
	
	
	for i in range(len(table)):
		widthArray.append(0)
		for j in table[i]:
			if widthArray[i] < len(j):
				widthArray[i] = len(j)

	for i in range(k):
		line = ''
		for j in range(len(table)):
			line += table[j][i].rjust(widthArray[j]+ 1)
		print(line)



printTable(tableData)
