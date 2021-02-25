import sys, select


userInput = ''

while 'exit' not in userInput: 
	print("You have five seconds to answer!")
	print('', end='')

	i, o, e = select.select( [sys.stdin], [], [], 5 )


	if (i):
		userInput = sys.stdin.readline().strip()
		print("Input is: ", userInput, '\n')
	else:
		print("no input\n")
		print(userInput)


# 	live.update(GenerateLayout(userInput))

# 	# print(userInput)
# 	# with term.cbreak():
# 	# 	while isLoop:
# 	# 		keypress = term.inkey()
# 	# 		if not keypress:
# 	# 			live.update(layout)
# 	# 		elif keypress.name == 'KEY_ESC':
# 	# 			isLoop = False
# 	# 		elif keypress.name == 'KEY_BACKSPACE':
# 	# 			userInput = userInput[:-1]
# 	# 		elif keypress.name == 'KEY_ENTER':
# 	# 			userInput = ''
# 	# 		else:
# 	# 			userInput = ''.join([userInput, str(keypress)])

# # print(layout)
