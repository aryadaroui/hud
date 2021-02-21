# from rich import pretty
from rich import prompt
from taskview import RichTaskGrid
from consoleview import ConsoleView
from calendarview import *
from rich import style, traceback
from rich import print
from rich.layout import Layout
from rich.panel import Panel
from task import Task, TaskList
from rich.prompt import Prompt

from rich.live import Live
from blessed import Terminal

traceback.install()


# test data
def GenerateLayout(string):
	tasks = TaskList()
	tasks._tasks.append(Task("video presentation again", "eecs 222", "Mar 01"))
	tasks._tasks.append(Task("hwk 1", "eecs 247", "Feb 18"))
	tasks._tasks[1].due = datetime.datetime(2021, 2, 10)
	tasks._tasks.append(Task("hwk3", "eecs222", "Mar 06"))


	# userConsole = ConsoleView()

	calendarView = Panel(Calendar.RichCalendarGrid(tasks), title="Calendar")
	overview = Panel("overview", title="Overview")
	taskView = Panel(RichTaskGrid(tasks), title="Tasks")
	consoleView = Panel(string, title="Console")

	layout = Layout()

	layout.split(
		Layout(name="upper"),
		Layout(taskView, name=taskView.title),
		Layout(consoleView, name=consoleView.title)
	)

	layout["upper"].split(
		Layout(calendarView, name=calendarView.title),
		Layout(overview, name=overview.title),
		direction="horizontal"
	)

	layout[calendarView.title].ratio = 2
	layout[consoleView.title].size = 4

	return layout

term = Terminal()

userInput = ''
isLoop = True

# print("\")
with Live(GenerateLayout(userInput), refresh_per_second=1/60, auto_refresh=False, redirect_stdout=False) as live:

	

	live.update(GenerateLayout(userInput))

	# print(userInput)
	# with term.cbreak():
	# 	while isLoop:
	# 		keypress = term.inkey()
	# 		if not keypress:
	# 			live.update(layout)
	# 		elif keypress.name == 'KEY_ESC':
	# 			isLoop = False
	# 		elif keypress.name == 'KEY_BACKSPACE':
	# 			userInput = userInput[:-1]
	# 		elif keypress.name == 'KEY_ENTER':
	# 			userInput = ''
	# 		else:
	# 			userInput = ''.join([userInput, str(keypress)])

# print(layout)
