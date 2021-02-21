from task import Task
from rich import traceback
from rich import print
from rich.table import Table
import datetime
from typing import List
from rich.console import Console

traceback.install()


#TODO make calendarview be init by a single tasklist object
class CalendarView():

	def __init__(self, tasks: List[Task]) -> None:
		self.tasks = tasks

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
		
		return monthLine

	def _DayCell(self) -> str:
		dayLine = ''

		for dayOffset in range(self.daysOut):
			day = datetime.datetime.today() + datetime.timedelta(days=dayOffset)
			if day.weekday() < 5:
				dayLine = ''.join([dayLine, '[blue]', day.strftime('%d'), '[/blue]  '])
			else:
				dayLine = ''.join([dayLine, '[red]', day.strftime('%d'), '[/red]  '])

		return dayLine

	@staticmethod
	def _ProgressCell(task: Task):
		'''
		docstring
		'''
		return ''.join(['▝', '▔▔▔▔' * (task.DaysLeft()+1),'▀▀'])



	# TODO: handle overdue tasks
	def RichGrid(self):
		'''
		docstring
		'''
		grid = Table.grid(expand=True)
		grid.add_column(justify='right', no_wrap=True)
		grid.add_column( no_wrap=True)
		grid.add_row(" ", " " + self._MonthCell())
		grid.add_row(" ", " " + self._DayCell())

		# this is a stupid way of doing this.
		# TODO fix tasklist architecture
		for task in self.tasks:
			# print(task.due)
			if task.DaysLeft() < self.daysOut - 1:

				if task.DaysLeft() < 0:
					grid.add_row(task.label, "▝[blink] OVERDUE ")				
				else:					
					grid.add_row(task.label, self._ProgressCell(task))
		grid.add_row(" ", " " + self._DayCell())
		grid.add_row(" ", " " + self._MonthCell())

		return grid



####### for testing

### Testing
# if True:

# 	tasks = [Task('label1', 'tag1', 'Feb 28', True), Task('label2', 'tag2', 'Feb 27', True), Task('label3', 'tag1', 'Mar 07', True), Task('label4', 'tag2', 'Feb 19 2021', True)]

# 	calendarView = CalendarView(tasks)
# 	console = Console()

# 	console.print(calendarView.RichGrid())