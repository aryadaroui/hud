import datetime
from typing import List

class Task():
	'''
	
	'''
	def __init__(self, label: str, tag: str, due: str, isOpen=True, color=None):
		self.label = label
		self.tag = tag
		self.color = color
		self.due = self.ParseDue(due)
		self.isOpen = isOpen
		self.isHidden = False

	def DaysLeft(self) -> int:
		timeDelta = self.due - datetime.datetime.today()
		return timeDelta.days
	
	# TODO more graceful error hadnlnig
	def ParseDue(self, due: str) -> datetime:
		'''
		takes input as "Feb 05"
		'''
		day = '  '
		month = '  '
		year = '    '

		for item in due.split(): # splits at spaces
			if item.isalpha():
				month = item
			elif len(item) < 4: # day of month
				day = item
			elif len(item) == 4: # year
				year = item
			else:
				raise Exception("bad date input\n")


		if year == '    ': # year was never set
			today =  datetime.datetime.today()

			date = datetime.datetime.strptime(''.join([due, ' ', today.strftime('%Y')]), '%b %d %Y')

			if date < today: # ie if it happened in the past
				# remake date for next year. recreating object keeps nice date out of range message
				date = datetime.datetime.strptime(''.join([due, ' ',  str(int(today.strftime('%Y')) + 1)]), '%b %d %Y')
		else:
			date = datetime.datetime.strptime(''.join([month, ' ', day, ' ', year]), '%b %d %Y')

		return date

	# Taskmanager depends on this which is stupid and i should fix later
	def __repr__(self) -> str:
		if self.isOpen:
			isOpenString = 'open'
		else:
			isOpenString = 'closed'
		
		return ''.join([self.label, '\t#', self.tag, '\t@', self.due.strftime('%b %d %Y'), '\t%', isOpenString])
		




tasks = [Task('a', 'taga', 'Mar 12'), Task('a', 'tavvv', 'Mar 15'), Task('b', 'tagcc', 'Mar 12'), Task('asd', 'taga', 'Mar 13')]

label = 'a'

filteredTasks = list(filter(lambda task: task.label == label, tasks))

print(filteredTasks)