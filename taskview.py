from rich import console
from task import Task, TaskList
from rich import align, traceback
from rich import print
from rich.table import Table
import datetime

from rich.console import Console
traceback.install()


def LineAndTag(task: Task):
	return '  ╰ ' + task.tag.text

def DaysAndDate(task: Task):
	return str(task.DaysLeft()).zfill(2) + " days   " + task.due.strftime('%b %d')
	
def ProgressBar(task: Task):
	string = ''
	if task.DaysLeft() < 0:
		string = "▕    [blink]OVERDUE[/blink]   ▏"
	else:
		string = ''.join(['▕', '█' * task.DaysLeft(), ' ' * (14 - task.DaysLeft()), '▏'])

	return string

def CircleAndTask(task: Task):
	string = ''

	if task.isOpen:
		string = ''.join(['○ ', task.text])
	else:
		string = ''.join(['● ', task.text])

	return string

task = Task('hoopty', 'doopty', 'Feb 25')


def RichTaskGrid(tasks: TaskList):
	grid = Table.grid(expand=True)
	grid.add_column(justify='left', no_wrap=True)
	grid.add_column(justify='right', no_wrap=True)
	for task in tasks._tasks:
		grid.add_row(CircleAndTask(task), ProgressBar(task))
		grid.add_row(LineAndTag(task), DaysAndDate(task))
		grid.add_row(" ", " ")

	return grid


# tasks = TaskList()
# tasks._tasks.append(Task("hwk 3", "eecs 247", "Feb 25"))
# # tasks._tasks[0].due = datetime.datetime(2021, 2, 14)
# tasks._tasks.append(Task("hwk 8", "eecs 222", "Mar 01"))



# console = Console()
# console.print(RichTaskGrid(tasks))



	
# print(CircleAndTask(task), ProgressBar(task))
# print(LineAndTag(task), DaysAndDate(task))
