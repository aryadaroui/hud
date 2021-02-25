
class Mode():
	'''
	docstring
	'''
	LABEL = 0
	TAG = 1
	DUE = 2

string = "add project 1  @Feb 21 #eecs 111"
label = ''
tag = ''
due = ''
mode = Mode.LABEL

# command =string[0:string.find(' ')] 
# print(command)

#

items = string.split()
command = items.pop(0)

# Parse arguments
for item in items:
	if item[0] == '#':
		mode = Mode.TAG
		item = item[1:]
	if item[0] == '@':
		mode = Mode.DUE
		item = item[1:]
	
	if mode == Mode.LABEL:
		label += item + ' '
	elif mode == Mode.TAG:
		tag += item + ' '
	elif mode == Mode.DUE:
			due += item + ' '


print("label: {}".format(label))
print("tag: {}".format(tag))
print("due: {}".format(due))


