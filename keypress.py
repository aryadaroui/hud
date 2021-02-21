import blessed
from blessed import *
# import psutil 
import os

# current_process = psutil.Process()
term = blessed.Terminal()




inputStr = ''
isLoop = True

with term.cbreak():
	while isLoop:
		keypress = term.inkey()
		if keypress.name == 'KEY_ESC':
			isLoop = False
		elif keypress.name == 'KEY_ENTER':
			inputStr = ''
		else:
			inputStr = inputStr + str(keypress)
		os.system('clear') 
		print("> " + inputStr)








# inputStr = ''

# keypress = term.inkey()
# if keypress.name == 'KEY_ENTER':
# 	inputStr = ''
# else:
# 	inputStr = inputStr + str(keypress)
# print("> " + inputStr)

# while keypress.name != 'KEY_ESCAPE':
# 	os.system('clear') 
# 	keypress = term.inkey()
# 	if keypress.name == 'KEY_ENTER':
# 		inputStr = ''
# 	else:
# 		inputStr = inputStr + str(keypress)
# 	print("> " + inputStr)

# print(">")sdd



# print(f"{term.home}{term.black_on_skyblue}{term.clear}"as
# print("press 'ESC' to quit.")
# with term.cbreak():
# 	# val = ''
# 	val = term.inkey(timeout=3)
# 	while val.name != 'KEY_ESCAPE':
# 		val = term.inkey(timeout=3)
# 		print(current_process.cpu_percent())
# 		if not val:
# 		   print("It sure is quiet in here ...")
# 		elif val.is_sequence:
# 		   print("got sequence: {0}.".format((str(val), val.name, val.code)))
# 		elif val:
# 		   print("got {0}.".format(val))
# 	print(f'bye!{term.normal}')
	