from task import Task
from rich import traceback
from rich import print
from rich.table import Table
import datetime
from taskmanager import TaskManager
from typing import List
from rich.console import Console

traceback.install()


#TODO make calendarview be init by a single tasklist object
class Overview():

	def __init__(self, tasks: List[Task]):
		self.tasks = tasks

	def RichGrid(self):
		'''
		docstring
		'''
		grid = Table.grid(expand=True)
		grid.add_column(justify='left', no_wrap=True)
		grid.add_column(justify='center', no_wrap=True)
		grid.add_column(justify='center', no_wrap=True)
		grid.add_column(justify='center', no_wrap=True)

		grid.add_row('[bold]Tags[/bold]', '[bold]Open[/bold]', '[bold]Closed[/bold]', '[bold]Hidden[/bold]')

		tags = [] # type: List[str]

		for task in self.tasks:
			tags.append(task.tag)
		tags = set(tags)			

		for tag in tags:
			grid.add_row(tag, str(self.TotalOpen(tag=tag)).zfill(2), str(self.TotalClosed(tag=tag)).zfill(2), str(self.TotalHidden(tag=tag)).zfill(2))
		grid.add_row('[bold]Total[/bold]', str(self.TotalOpen()).zfill(2), str(self.TotalClosed()).zfill(2), str(self.TotalHidden()).zfill(2))

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
		return count

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
		return count

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
		return count	





####### for testing

### Testing
# if testing:

# 	# tasks = [Task('label1', 'tag1', 'Feb 28', True), Task('label2', 'tag2', 'Feb 27', True), Task('label3', 'tag1', 'Mar 07', True), Task('label4', 'tag2', 'Feb 19 2021', True)]

# 	taskManager = TaskManager()

# 	overview = Overview(taskManager.LoadTasks())
# 	console = Console()

# 	console.print(overview.RichGrid())