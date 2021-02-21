from task import Task
from rich import traceback
from rich.table import Table
from typing import List

from rich.console import Console
traceback.install()

class TaskView():
	'''
	docstring
	'''
	def __init__(self, tasks: List[Task], groupByTag=False):
		self.tasks = tasks
		self.groupByTag = groupByTag

	def _LabelCell(self, task: Task):
		'''
		○ task label
		'''
		string = ''

		if task.isOpen:
			string = ''.join(['○ ', task.label])
		else:
			string = ''.join(['● ', task.label])

		return string

	def _TagCell(self, task: Task):
		'''
		  ╰ task tag
		'''
		return '  ╰ ' + task.tag


	def _DayCell(self, task: Task):
		return str(task.DaysLeft()).zfill(2) + " days   " + task.due.strftime('%b %d')


	def _ProgressCell(self, task: Task):
		'''
		████
		'''
		#TODO fix widths and shape for > 14 days
		daysLeft = task.DaysLeft()
		string = ''
		if daysLeft < 0:
			string = "▕    [blink]OVERDUE[/blink]   ▏"
		elif daysLeft > 14:
			string = "▐█████████████＋"
		else:
			string = ''.join(['▕', '█' * daysLeft, ' ' * (14 - daysLeft), '▏'])

		return string

	def RichGrid(self) -> Table:
		'''
		TODO example
		'''
		grid = Table.grid(expand=True)

		if self.groupByTag:
			grid.add_column(justify='left', no_wrap=True)
			grid.add_column(justify='right', no_wrap=True)
			grid.add_column(justify='right', no_wrap=True)

			tags = [] # type: List[str]

			for task in self.tasks:
				tags.append(task.tag)
			tags = set(tags)

			for tag in tags:
				grid.add_row(tag)
				for task in self.tasks:
					if tag == task.tag:
						grid.add_row(self._LabelCell(task), self._DayCell(task), self._ProgressCell(task))
				grid.add_row('','','')

		else:
			grid.add_column(justify='left', no_wrap=True)
			grid.add_column(justify='right', no_wrap=True)
			for task in self.tasks:
				grid.add_row(self._LabelCell(task), self._ProgressCell(task))
				grid.add_row(self._TagCell(task), self._DayCell(task))
				grid.add_row(" ", " ")
		return grid


# ### Testing
# if True:

# 	tasks = [Task('label1', 'tag1', 'Feb 28', True), Task('label2', 'tag2', 'Feb 27', True), Task('label3', 'tag1', 'Mar 09', True), Task('label4', 'tag2', 'Feb 19 2021', True)]

# 	taskView = TaskView(tasks, False)
# 	console = Console()

# 	console.print(taskView.RichGrid())