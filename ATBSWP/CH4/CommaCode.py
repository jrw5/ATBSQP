import copy

spam = ['apples', 'bananas', 'tofu', 1]
#spam = []
#spam = ['Dogs']

length = len(spam)

spamString = ''
if len(spam) == 0:
	print('This is an empty List')
elif(len(spam)) == 1:
	spamString = str(spam[0])
else:
	while len(spam) > 0:
		if length == len(spam):
			spamString = 'and ' + str(spam[-1])
		else:
			spamString = str(spam[-1]) + ', ' + spamString
		del spam[-1]
	print(spamString)