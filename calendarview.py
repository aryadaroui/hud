from task import TaskList
from rich import traceback
from rich import print
from rich.table import Table
import datetime

traceback.install()


#TODO make calendarview be init by a single tasklist object
class Calendar():
	@staticmethod
	def MonthLine() -> str:
		
		monthLine = ''

		for dayOffset in range(14):
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

	@staticmethod
	def DayLine() -> str:
		dayLine = ''

		for dayOffset in range(14):
			day = datetime.datetime.today() + datetime.timedelta(days=dayOffset)
			dayLine = ''.join([dayLine, day.strftime('%d'), '  '])
		return dayLine


	# TODO: handle overdue tasks
	@staticmethod
	def RichCalendarGrid(tasks: TaskList):
		'''
		docstring
		'''
		grid = Table.grid(expand=True)
		grid.add_column(justify='right', no_wrap=True)
		grid.add_column( no_wrap=True)
		grid.add_row(" ", " " + Calendar.MonthLine())
		grid.add_row(" ", " " + Calendar.DayLine())

		# this is a stupid way of doing this.
		# TODO fix tasklist architecture
		for task in tasks._tasks:
			# print(task.due)
			if task.DaysLeft() < 14:

				if task.DaysLeft() < 0:
					grid.add_row(task.text, "▝[blink] OVERDUE ")				
				else:					
					grid.add_row(task.text, ''.join(['▝', '▔▔▔▔' * (task.DaysLeft()+1),'▀▀']))
		grid.add_row(" ", " " + Calendar.DayLine())
		grid.add_row(" ", " " + Calendar.MonthLine())

		return grid



####### for testing

# tasks = TaskList()
# tasks._tasks.append(Task("hwk 3", "eecs 247", "Feb 18"))
# tasks._tasks[0].due = datetime.datetime(2021, 2, 14)
# tasks._tasks.append(Task("hwk 8", "eecs 222", "Mar 01"))


# console = Console()
# console.print(Calendar.RichCalendarGrid(tasks))


# print(Calendar.MonthLine())
# print(Calendar.DayLine())