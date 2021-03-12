from dataclasses import dataclass
import sys
import select
import datetime
from rich import table
from rich.console import ConsoleRenderable
from rich.table import Table
from rich.live import Live

from taskmanager import TaskManager


class InputManager():
	'''
	docstring
	'''
	def __init__(self, taskManager: TaskManager) -> None:
		self.userInput = ''
		self.output = ''
		self.taskManager = taskManager

	def IO_Prompt(self):
		'''
		docstring
		'''
		self.userInput = ''
		loop = True

		i, o, e = select.select( [sys.stdin], [], [], 3600) # nonblocking input. last arg is timeout time in seconds

		# print(">")

		if (i):
			self.userInput = sys.stdin.readline().strip()
			self._ExecuteInput(self.userInput)
			# live.refresh()
			# print("good", userInput)
		else:
			self.output = ''
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
		grid.add_column(justify='right', no_wrap=True)

		grid.add_row(self.output, datetime.datetime.now().strftime('%H:%M:%S'), style='green')
		return grid
		
		

	def _ExecuteInput(self, inputString: str):
		'''
		docstring
		'''
		class Mode():
			label = 'label'
			tag = 'tag'
			due = 'due'

		mode = Mode.label
		label = ''
		tag = ''
		due = ''
		items = inputString.lower().split()
		command = items.pop(0)

		# Parse arguments
		for item in items:
			if item[0] == '#':
				mode = Mode.tag
				item = item[1:]
			if item[0] == '@':
				mode = Mode.due
				item = item[1:]
			
			if mode == Mode.label:
				label += item + ' '
			elif mode == Mode.tag:
				tag += item + ' '
			elif mode == Mode.due:
					due += item + ' '

		label = label.strip()
		tag = tag.strip()
		due = due.strip()

		if command == 'add':
			self.output = self.taskManager.Add(label, tag, due)
		elif command == 'close':
			self.output = self.taskManager.Close(label, tag)
		elif command == 'open':
			self.output = 'open'
		elif command == 'delete':
			self.output = self.taskManager.Delete(label, tag)
		elif command == 'toggle':
			# self.output = 'toggle'
			self.taskManager.Toggle(label, tag)
		else:
			self.output = 'bad command'


		


	def RandomEmoji(happy=True):
		'''
		docstring
		'''
		happy = ()
		sad = ()
		