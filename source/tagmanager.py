from rich import traceback
from task import Task
from typing import List
import re
traceback.install()
from rich import print


class TagManager():
	'''
	docstring
	'''



	def __init__(self):
		self.filePath = "/Users/aryadaroui/Documents/GitHub/hud/tags.txt"
		self.tags = self.LoadTags()

	# def __init__(self, tasks: List[Task]):
	# 	self.filePath = "/Users/aryadaroui/Documents/GitHub/hud/tags.txt"
	# 	self.tags = self.LoadTags()

	def LoadTags(self) -> dict:
		'''
		docstring
		'''
		with open(self.filePath) as file:
			lines = file.readlines()

		tags = {}

		for line in lines:
			line = line.strip('\n')
			items = re.split(r'\t+', line)
			items = [i for i in items if i != '']
			if items != []: # ignore empty lines
				tags[items[0]] = items[1]


		return tags


	def SaveTags(self):
		'''
		docstring
		'''
		with open(self.filePath, 'w') as file:
			for tag, color in self.tags.items():
				file.write(''.join([tag, '\t', color, '\n']))

	def EditColor(self, tag: str, color: str):
		'''
		docstring
		'''
		pass


		

	def UpdateTags(self, tasks: List[Task]):
		'''
		docstring
		# '''
		# loadedTags = self.LoadTags()

		# tags = [] # type: List[str]

		# for task in self.tasks:
		# 	tags.append(task.tag)
		# tags = set(tags)
		pass

### Testing
# if True:
# 	tasks = [Task('label1', 'tag1', 'Feb 28', True), Task('label2', 'tag2', 'Feb 27', True), Task('label3', 'tag1', 'Mar 07', True), Task('label4', 'tag2', 'Feb 19 2021', True)]

# 	tagManager = TagManager(tasks)
# 	tagManager.SaveTags()

	# print(tagManager.LoadTags())