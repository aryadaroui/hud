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
		self.tasks = sorted(tasks, key=lambda x: x.DaysLeft(), reverse=False)
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
		return str(task.DaysLeft()+1).zfill(2) + " days   " + task.due.strftime('%b %d')


	def _ProgressCell(self, task: Task):
		'''
		████
		'''
		#TODO fix widths and shape for > 14 days
		daysLeft = task.DaysLeft()
		string = ''


		if daysLeft < 0 and task.isOpen:
			string = "[underline][deep_pink2]▏   [deep_pink2] LATE    [/deep_pink2]▕[/underline]"
		elif daysLeft < 0:
			string = "[underline]▏            ▕[/underline]"

		elif daysLeft > 13:
			string = "[underline][reverse]            ＋[/reverse][/underline]"
		elif daysLeft == 13:
			string = ''.join(['[frame][underline]', '█' * (daysLeft + 1), ' ' * (14 - daysLeft), '[/frame][/underline]'])
		else:
			string = ''.join(['[frame][underline]', '█' * (daysLeft + 1), ' ' * (14 - daysLeft -2), '▕[/frame][/underline]'])

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

			# tags = [] # type: List[str]
			

			# for task in self.tasks:
			# 	tags.append(task.tag)
			# tags = set(tags)

			tags = {}
			count = 0
			style = ''

			for task in self.tasks:
				if task.tag not in tags:
					tags[task.tag] = task.color

			# ⦸ ◌ could use either of these for hidden symbol

			for tag in tags:
				grid.add_row(''.join(['[{color}]'.format(color=tags[tag]), tag, '[/{color}]'.format(color=tags[tag])]), '', '○ ' + self.TotalOpen(tag=tag)  + ' ● ' + self.TotalClosed(tag=tag) + ' ⦸ ' + self.TotalHidden(tag=tag), style='underline {color}'.format(color=tags[tag]))
				for task in self.tasks:
					if tag == task.tag:
						count += 1
						if count % 2:
							style = 'grey85'
						else:
							style = 'grey70'
						grid.add_row('  ' + self._LabelCell(task), self._DayCell(task), self._ProgressCell(task), style=style)
				count = 0
				grid.add_row('','','')

		else:
			grid.add_column(justify='left', no_wrap=True)
			grid.add_column(justify='right', no_wrap=True)
			for task in self.tasks:
				grid.add_row(self._LabelCell(task), self._ProgressCell(task))
				grid.add_row(self._TagCell(task), self._DayCell(task))
				grid.add_row(" ", " ")
		return grid

	def TotalClosed(self, tag=None):
		'''
		docstring
		'''
		count = 0
		if tag == None:
			for task in self.tasks:
				if task.isOpen == False:
					count += 1
		else:
			for task in self.tasks:
				if task.isOpen == False and task.tag == tag:
					count += 1
		return str(count).zfill(2)

	def TotalOpen(self, tag=None):
		'''
		docstring
		'''
		count = 0
		if tag == None:
			for task in self.tasks:
				if task.isOpen == True:
					count += 1
		else:
			for task in self.tasks:
				if task.isOpen == True and task.tag == tag:
					count += 1
		return str(count).zfill(2)

	def TotalHidden(self, tag=None):
		'''
		docstring
		'''
		count = 0
		if tag == None:
			for task in self.tasks:
				if task.isHidden == True:
					count += 1
		else:
			for task in self.tasks:
				if task.isHidden == True and task.tag == tag:
					count += 1
		return str(count).zfill(2)

# ### Testing
# if True:

# 	tasks = [Task('label1', 'tag1', 'Feb 28', True), Task('label2', 'tag2', 'Feb 27', True), Task('label3', 'tag1', 'Mar 09', True), Task('label4', 'tag2', 'Feb 19 2021', True)]

# 	taskView = TaskView(tasks, False)
# 	console = Console()

# 	console.print(taskView.RichGrid())