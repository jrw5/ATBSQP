#bulletPointAdder.py
#Joel Wheatley
#1/15/20

#Paste text from a clipboard
#Do something to it
#Copy the text to the new clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Seperate lines and add stars


#seperate lines and add stars

lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '*' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)

print(text)