#Joel Wheatley
#1/14/2020
#Create a program that displays and adds things to a fantasy game inventory


stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
	print("inventory:")
	item_total =0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("Total Number of Items: " + str(item_total))



def addToInventory(inventory, addedItems):
	for item in addedItems:
		if item in inventory.keys():
			inventory[item] += 1
		else:
			inventory[item] = 1

displayInventory(stuff)

addToInventory(stuff, dragonLoot)

displayInventory(stuff)