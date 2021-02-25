from typing import List
from task import Task
from tagmanager import TagManager
import re

# from main import testing



class TaskManager():
	'''
	docstring
	'''
	def __init__(self):
		self.filePath = "/Users/aryadaroui/Documents/GitHub/hud/tasks.txt"
		self.tasks = self.LoadTasks()
		self.tagManager = TagManager()
		self.LoadAndSetTasksColors()

	# def  __init__(self, tasks: List[Task]):
	# 	self.tasks = tasks
	# 	self.tagManager = TagManager(self.tasks)
	# 	self.filePath = "/Users/aryadaroui/Documents/GitHub/hud/tasks.txt"

	def LoadAndSetTasksColors(self):
		'''
		sets the colors for self.tasks. This changes self.tasks; does not return anything
		'''
		tags = self.tagManager.LoadTags()

		for task in self.tasks:
			if task.tag in tags:
				task.color = tags[task.tag]
			else:
				task.color = 'white'

		# a = 1

	

	def Delete(self, label: str, tag: str):
		'''
		
		'''
		pass

	def DeleteOld(self):
		'''
		docstring
		'''
		pass

	def DeleteAll(self):
		'''
		docstring
		'''
		pass

	def HideOld(self):
		'''
		docstring
		'''
		pass

	def HideClosed(self):
		'''
		docstring
		'''
		pass

	def Edit(self):
		'''
		docstring
		'''
		pass

	def Sort(self):
		'''
		docstring
		'''
		pass

	def LoadTasks(self) -> List[Task]:
		with open(self.filePath) as file:
			lines = file.readlines()

			# print(lines)

		tasks = [] # type: list[Task]

		for line in lines:
			line = line.strip('\n')
			items = re.split(r'\t+', line)

			items = [i for i in items if i != ''] 

			if items == ['task', '#tag', '@due', '%status'] or items == []:
				pass
			else:
				for item in items:
					firstChar = item[0]
					if firstChar == '#':
						tag = item[1:]
					elif firstChar == '@':
						due = item[1:]
					elif firstChar == '%':
						if item[1:] == 'closed':
							isOpen = False
						else:
							isOpen = True
					else:
						taskName = item
				tasks.append(Task(taskName, tag, due, isOpen))
		return tasks

	def SaveTasks(self, tasks: List[Task]):

		with open(self.filePath, 'w') as file:
			file.write('task\t#tag\t@due\t%status\n\n')
			for task in tasks:
				file.write(''.join([task.__repr__(), '\n']))

				


### Testing
if False:
	taskManager = TaskManager()
	tasks = taskManager.LoadTasks()
	print(tasks)