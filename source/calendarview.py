from task import Task
from rich import traceback
from rich import print
from rich.table import Table
import datetime
from typing import List
from rich.console import Console

from taskmanager import TaskManager

traceback.install()


#TODO make calendarview be init by a single tasklist object
class CalendarView():

	def __init__(self, taskManager: TaskManager) -> None:
		self.taskManager = taskManager # passed by 'reference'. do not alter
		self.daysOut = 14 # how many days ahead to display

	def _MonthCell(self) -> str:
		monthLine = ''


		for dayOffset in range(self.daysOut):
			# print(day)
			day = datetime.datetime.today() + datetime.timedelta(days=dayOffset)

			if dayOffset == 0:
				# print(day.strftime('%b'), end=' ')
				monthLine = ''.join([monthLine, day.strftime('%b'), ' '])
			elif day.strftime('%d') == '01':
				# print(day.strftime('%b'), end=' ')
				monthLine = ''.join([monthLine, day.strftime('%b'), ' '])
			else:
				# print('    ', end='')
				monthLine = ''.join([monthLine, '    '])
		
		return ' [grey70]' + monthLine + '[/grey70]'

	def _DayCell(self) -> str:
		dayLine = ''

		for dayOffset in range(self.daysOut):
			day = datetime.datetime.today() + datetime.timedelta(days=dayOffset)
			if day.weekday() < 5: # weekday
				dayLine = ''.join([dayLine, '[grey42]', day.strftime('%d'), '[/grey42]  '])
			else: # weekend
				dayLine = ''.join([dayLine, '[grey70]', day.strftime('%d'), '[/grey70]  '])

		return ' ' + dayLine


	def _ProgressCell(self, task: Task):
		'''
		docstring
		'''
		string = ''

		if task.DaysLeft() < 0:
			string = ''.join(["[deep_pink2]  LATE                                                    ", '[{color}]'.format(color=task.color), task.tag, '[/{color}]'.format(color=task.color)])		
		else:					
			string = ''.join(['  ', '────' * (task.DaysLeft()+1),'▬▬', '[black]' + '────'*(14-task.DaysLeft()-1-1) + ' [/black] ' + ''.join(['[{color}]'.format(color=task.color), task.tag, '[/{color}]'.format(color=task.color)])])

		return string

	# TODO: handle overdue tasks
	# NOTE:
	def RichGrid(self):
		'''
		docstring
		'''
		tasks = self.taskManager.tasks
		tasks = sorted(tasks, key=lambda task: task.DaysLeft(), reverse=False)

		grid = Table.grid(expand=True)
		grid.add_column(justify='right', no_wrap=True, max_width=16)
		grid.add_column(justify='left', no_wrap=True)
		# grid.add_column(justify='left', no_wrap=True)
		# grid.add_column(justify='left', no_wrap=True)
		grid.add_row(" ", " " + self._MonthCell())
		grid.add_row(" ", " " + self._DayCell())

		for task in tasks:
			if task.DaysLeft() < self.daysOut - 1 and task.isOpen:			
				grid.add_row(task.label, self._ProgressCell(task))
		# grid.add_row(" ", " " + self._DayCell()+ '')
		# grid.add_row(" ", " " + self._MonthCell()+ '')

		return grid



####### for testing

### Testing
# if True:

# 	tasks = [Task('label1', 'tag1', 'Feb 28', True), Task('label2', 'tag2', 'Feb 27', True), Task('label3', 'tag1', 'Mar 07', True), Task('label4', 'tag2', 'Feb 19 2021', True)]

# 	calendarView = CalendarView(tasks)
# 	console = Console()

# 	console.print(calendarView.RichGrid())