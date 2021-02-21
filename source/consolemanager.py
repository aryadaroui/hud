from blessed import Terminal



class Mode():

	MAIN = 'MAIN'
	ADD = 'ADD'
	EDIT = 'EDIT'
	DELETE = 'DELETE'


class InputManager():

	def __init__(self):
		self.mode = Mode.MAIN
		self.userInput = ''
		# self.selection = None
		# self.subSelection = None

	def KeyCapture(self):
		isLoop = True
		term = Terminal()
		with term.cbreak():
			while isLoop:
				keypress = term.inkey()
				if keypress.name == 'KEY_ESC':
					isLoop = False
				elif keypress.name == 'KEY_BACKSPACE':
					self.userInput = self.userInput[:-1]
				elif keypress.name == 'KEY_ENTER':
					self.userInput = ''
				else:
					self.userInput = self.userInput + str(keypress)
				# print(''.join(['> ', self.userInput]))
