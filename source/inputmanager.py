from dataclasses import dataclass
import sys
import select
import datetime
from rich import table
from rich.console import ConsoleRenderable
from rich.table import Table
from rich.live import Live


class InputManager():
	'''
	docstring
	'''
	def __init__(self) -> None:
		self.userInput = ''
		self.output = ' Howdy your input was '

	def IO_Prompt(self):
		'''
		docstring
		'''
		self.userInput = ''
		loop = True

		i, o, e = select.select( [sys.stdin], [], [], 10 ) # nonblocking input

		# print(">")

		if (i):
			self.userInput = sys.stdin.readline().strip()
			self._ExecuteInput(self.userInput)
			# live.refresh()
			# print("good", userInput)
		# else:
		# 	self.output = 'no input'
		# 	# live.refresh()
		# 	# print("bad")
		if self.userInput == 'exit':
			loop = False

		return loop


	def RichGrid(self):
		'''
		Returns grid with output prompt on left and time on right.
		'''
		grid = Table.grid(expand=True)
		grid.add_column(justify='left')
		grid.add_column(no_wrap=True)

		grid.add_row(self.output, datetime.datetime.now().strftime('%H:%M:%S'), style='green')
		return grid
		
		

	def _ExecuteInput(self, inputString: str):
		'''
		docstring
		'''
		inputString.split()



	def RandomEmoji(happy=True):
		'''
		docstring
		'''
		happy = ()
		sad = ()
		