# from rich import pretty
from rich.console import Console
from inputmanager import InputManager
from rich import prompt
from rich.align import AlignMethod
from rich.console import JustifyMethod
# from taskview import RichTaskGrid
# from consoleview import ConsoleView
from calendarview import *
from rich import style, traceback
from rich import print
from rich.layout import Layout
from rich.panel import Panel
# from task import Task, TaskList
# from rich.prompt import Prompt

from rich.live import Live
from blessed import Terminal


from taskmanager import *
from overview import *
from taskview import *
import time
# from datetime import datetime

from inputadvanced import inputAdv


import sys
import select
import datetime

traceback.install()


# italicize tags wher available

class LiveLayoutView():
	'''
	docstring
	'''


	### TODO, send taskmanager itself for a single source of truth.


	def __init__(self) -> None:
		self.groupByTag = True
		self.taskManager = TaskManager()
		self.calendarView = CalendarView(self.taskManager)
		# self.overview = Overview(self.taskManager.tasks)
		self.taskView = TaskView(self.taskManager, groupByTag=self.groupByTag)
		# self.layout = self.MakeLayout()
		self.inputManager = InputManager(self.taskManager)
		self.loop = True
		# self.input = ''

	def RichLayout(self) -> Layout:
		layout = Layout()
		layout.split(
		# Layout(name="upper"),
		Layout(" ", name="BufferTop"),
		Layout(Panel(self.calendarView.RichGrid(), title="Calendar", style='grey50'), name="Calendar"),
		Layout(Panel(self.taskView.RichGrid(), title="Tasks", style= 'grey50'), name="Tasks"),
		# Layout(Panel(str(datetime.now()), title="Console"), name="Console")
		Layout(self.inputManager.RichGrid(), name='Console')
		# Layout(" ", name="BufferBot")
		# Layout(datetime.datetime.now().strftime('%H:%M:%S') + '    ' + self.input, name='Console')
		)

		# layout["upper"].split(
		# 	Layout(Panel(self.calendarView.RichGrid(), title="Calendar"), name="Calendar"),
		# 	# Layout(Panel(self.overview.RichGrid(), title="Overview"), name="Overview"),
		# 	direction="horizontal"
		# )		


		# layout['Calendar'].ratio = 2.5
		# layout['Overview'].ratio = 
		layout["BufferTop"].size = 1
		layout["Tasks"].ratio = 1.5
		# layout["BufferBot"].size = 1
		layout['Console'].size = 1
		return layout

	def LiveRender(self):
		'''
		docstring
		'''
		# term = Terminal()

		# print(self.RichLayout())
		# while True:

		response = ''
		initial = ''
		timedOut = False

		console = Console()

		with Live(console=console, auto_refresh=False, screen=True, vertical_overflow='ellipsis', redirect_stdout=False, redirect_stderr=False) as live:
			# term.inkey(timeout=5)
			live.update(self.RichLayout(), refresh=True)

			while response != 'exit':
				response, timedOut = inputAdv('', initial, 3600)
				if timedOut:
					initial = response
				else:
					initial = ''
					self.inputManager._ExecuteInput(response.strip())
				live.update(self.RichLayout(), refresh=True)

			# while self.loop:
			# 	self.loop = self.inputManager.IO_Prompt() # returns false if user inputs exit. TODO: this isn't an explicit way of showing IO is being done here. should change.
			# 	live.update(self.RichLayout(), refresh=True)



			# while True:
			# 	i, o, e = select.select( [sys.stdin], [], [], 5 ) # nonblocking input

			# 	if (i):
			# 		self.input = sys.stdin.readline()
			# 		print("yes input")
			# 	else:
			# 		print("no input")
			# 	live.update(self.RichLayout(), refresh=True)


