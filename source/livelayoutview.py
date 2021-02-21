# from rich import pretty
from rich import prompt
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
from datetime import datetime

traceback.install()



class LiveLayoutView():
	'''
	docstring
	'''
	def __init__(self) -> None:
		self.groupByTag = True
		self.taskManager = TaskManager()
		self.calendarView = CalendarView(self.taskManager.tasks)
		self.overview = Overview(self.taskManager.tasks)
		self.taskView = TaskView(self.taskManager.tasks, groupByTag=self.groupByTag)
		# self.layout = self.MakeLayout()


	def RichLayout(self) -> Layout:
		layout = Layout()
		layout.split(
		Layout(name="upper"),
		Layout(Panel(self.taskView.RichGrid(), title="Tasks"), name="Tasks"),
		Layout(Panel(str(datetime.now()), title="Console"), name="Console")
		)

		layout["upper"].split(
			Layout(Panel(self.calendarView.RichGrid(), title="Calendar"), name="Calendar"),
			Layout(Panel(self.overview.RichGrid(), title="Overview"), name="Overview"),
			direction="horizontal"
		)		


		layout['Tasks'].ratio = 2
		layout['Console'].size = 4
		return layout

	def LiveRender(self):
		'''
		docstring
		'''
		# term = Terminal()

		# print(self.RichLayout())
		while True:
			with Live(self.RichLayout(), auto_refresh=False, screen=True, vertical_overflow='ellipsis') as live:
				# term.inkey(timeout=5)

				time.sleep(60)
				live.refresh()



		





# # test data
# def GenerateLayout():
# 	tasks = TaskList()
# 	tasks._tasks.append(Task("video presentation again", "eecs 222", "Mar 01"))
# 	tasks._tasks.append(Task("hwk 1", "eecs 247", "Feb 18"))
# 	tasks._tasks[1].due = datetime.datetime(2021, 2, 10)
# 	tasks._tasks.append(Task("hwk3", "eecs222", "Mar 06"))


# 	# userConsole = ConsoleView()

# 	calendarView = Panel(CalendarView.RichCalendarGrid(tasks), title="Calendar")
# 	overview = Panel("overview", title="Overview")
# 	taskView = Panel(RichTaskGrid(tasks), title="Tasks")
# 	consoleView = Panel("string", title="Console")

# 	layout = Layout()

# 	layout.split(
# 		Layout(name="upper"),
# 		Layout(taskView, name=taskView.title),
# 		Layout(consoleView, name=consoleView.title)
# 	)

# 	layout["upper"].split(
# 		Layout(calendarView, name=calendarView.title),
# 		Layout(overview, name=overview.title),
# 		direction="horizontal"
# 	)

# 	layout[calendarView.title].ratio = 2
# 	layout[consoleView.title].size = 4

# 	return layout

# term = Terminal()

# userInput = ''
# isLoop = True

# # print("\")
# with Live(GenerateLayout(userInput), refresh_per_second=1/60, auto_refresh=False, redirect_stdout=False) as live:

	

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
