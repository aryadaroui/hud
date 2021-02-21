from rich import print, traceback
from task import *
import re

traceback.install()



def LoadTasks(filename: str) -> List[Task]:
	with open(filename) as file:
		lines = file.readlines()

		# print(lines)

	tasks = [] # type: List[Task]

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
				



		# tasks.append
		
	
def SaveTasks(filename: str, tasks: List[Task]):

	with open(filename, 'w') as file:
		file.write('task\t#tag\t@due\t%status\n\n')
		for task in tasks:
			file.write(''.join([task.__repr__(), '\n']))

	

def LoadColors(filename: str) -> dict:
	pass

def SaveColors(filename: str):
	pass

tasks = LoadTasks('tasks.txt')

SaveTasks('savetasktest.txt', tasks)
