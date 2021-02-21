import datetime
from typing import List


class Color():
	RED = (128, 32, 64)


class Tag():
	def __init__(self):
		self.text = ''
		self.color = Color.RED

	def __init__(self, text: str, color: Color):
		self.text = text
		self.color = Color.RED


class Task():
	'''
	
	'''
	def __init__(self):
		self.text = ''
		self.tag = Tag()
		self.due = datetime.datetime.today() + datetime.timedelta(days=7)
		self.isOpen = True
		self.isHidden = False

	def __init__(self, text: str, tag: str, due: str, isOpen: bool):
		self.text = text
		self.tag = Tag(tag, Color.RED)
		# self.due = datetime.strptime(due, '%b %d')
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

		# datetime.datetime.strptime(due, '%b %d')

	def __repr__(self) -> str:
		if self.isOpen:
			isOpenString = 'open'
		else:
			isOpenString = 'closed'
		
		return ''.join([self.text, '\t#', self.tag.text, '\t@', self.due.strftime('%b %d %Y'), '\t%', isOpenString])
		

class TaskList():
	'''
	docstring
	'''
	def __init__(self):
		self._tasks = [] # type: List[Task]


	def Delete(self, index=None, target=None,):
		'''
		target="old": closed and > 1 week due date
		target="closed": all closed
		target="all": delete everything
		'''
		pass

	def Add(self, task: Task):
		'''
		'''
		pass

	def Hide(self, ):
		'''
		docstring
		'''
		pass



### testing


# task = Task("hwk 3", "eecs 247", "Feb 28")

# print(task.due)