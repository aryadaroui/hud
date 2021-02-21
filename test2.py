import time

from rich.live import Live
from rich.table import Table
from rich.prompt import Prompt

from blessed import Terminal

term = Terminal()

table = Table()
table.add_column("Row ID")
table.add_column("Description")
table.add_column("Level")

import time


# import _thread
# import threading

# def raw_input_with_timeout(prompt, timeout=30.0):
#     print(prompt, end=' ')    
#     timer = threading.Timer(timeout, _thread.interrupt_main)
#     astring = None
#     try:
#         timer.start()
#         astring = input(prompt)
#     except KeyboardInterrupt:
#         pass
#     timer.cancel()
#     return astring


# raw_input_with_timeout("testing: ", timeout= 3)

term = Terminal()


while True:
	with Live(table, auto_refresh=False, screen=True) as live:  # update 4 times a second to feel fluid
		a = term.inkey(timeout=5)
		if not a:
			for row in range(5):
				# live.console.print("Working on row #{row}")
				print(time.time())
				table.add_row(f"{row}", f"description {row}", "[red]ERROR")
				# Prompt.ask("test")
				live.refresh()
				time.sleep(0.5)



# inputStr = ''
# isLoop = True

# with term.cbreak():
# 	while isLoop:
# 		keypress = term.inkey()
# 		if keypress.name == 'KEY_ESC':
# 			isLoop = False
# 		elif keypress.name == 'KEY_ENTER':
# 			inputStr = ''
# 		else:
# 			inputStr = inputStr + str(keypress)
# 		os.system('clear') 
# 		print("> " + inputStr)