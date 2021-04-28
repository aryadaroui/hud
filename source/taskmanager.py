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
		self.filePath = "/Users/aryadaroui/Documents/Code/hud/tasks.txt"
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

	def Add(self, label, tag, due):
		'''
		docstring
		'''

		status = ''

		if label != '':
			self.tasks.append(Task(label, tag, due))
			self.SaveTasks(self.tasks)
			self.LoadAndSetTasksColors()
			status = 'added: {label} #{tag} @{due}'.format(label=label, tag=tag, due=due)


		return status


	def Delete(self, label: str, tag: str):
		'''
		
		'''
		# TODO: does not detect if duplicates under same tag

		status = ''
		label = label.strip()
		tag = tag.strip()

		if tag == '':
			filteredTasks = list(filter(lambda task: task.label == label, self.tasks))
			if len(filteredTasks) == 1:
				self.tasks.remove(filteredTasks[0])
				self.SaveTasks(self.tasks)
				status = "deleted task: {task}".format(task=filteredTasks[0])
			elif len(filteredTasks) > 1:
				status = "need tag to clarify"
			else:
				status = "could not find label"
		else:
			filteredTasks = list(filter(lambda task: task.label == label and task.tag == tag, self.tasks))
			if len(filteredTasks) == 1:
				self.tasks.remove(filteredTasks[0])
				self.SaveTasks(self.tasks)
				status = "deleted task: {task}".format(task=filteredTasks[0])
			elif len(filteredTasks) > 1:
				status = "duplicates detected. deleted one task: {task}".format(task=filteredTasks[0])
				self.tasks.remove(filteredTasks[0])
				self.SaveTasks(self.tasks)
			else:
				status = "could not find label"

		return status

		# for task in self.tasks:

		# self.tasks.remove(Task(label, tag, due,))

	def Close(self, label: str, tag: str):

		status = ''
		label = label.strip()
		tag = tag.strip()

		if tag == '':
			filteredTasks = list(filter(lambda task: task.label == label, self.tasks))
			if len(filteredTasks) == 1:
				self.tasks[self.tasks.index(filteredTasks[0])].isOpen = False
				# self.tasks.remove(filteredTasks[0])
				self.SaveTasks(self.tasks)
				status = "closed task: {task}".format(task=filteredTasks[0])
			elif len(filteredTasks) > 1:
				status = "need tag to clarify"
			else:
				status = "could not find label"
		else:
			filteredTasks = list(filter(lambda task: task.label == label and task.tag == tag, self.tasks))
			if len(filteredTasks) == 1:
				self.tasks[self.tasks.index(filteredTasks[0])].isOpen = False
				self.SaveTasks(self.tasks)
				status = "closed task: {task}".format(task=filteredTasks[0])
			elif len(filteredTasks) > 1:
				status = "duplicates detected. clozed one task: {task}".format(task=filteredTasks[0])
				self.tasks.remove(filteredTasks[0])
				self.SaveTasks(self.tasks)
			else:
				status = "could not find label"
		return status

	def Hid(self):
		'''
		Hide old and hide
		'''
		pass

	def Edit(self):
		'''
		docstring
		'''
		pass

	def LoadTasks(self) -> List[Task]:
		with open(self.filePath) as file:
			lines = file.readlines()

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