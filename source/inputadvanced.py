import readline
import signal


def _handler(signum, frame):
	'''
	Generic handler that is passed to signal module for async input, allowing time out
	### parameters
	`signum:` signal number
	`frame:` current stack frame
	'''
	raise TimeoutError()

def inputAdv(prompt: str, initInput: str = '', timeout: int = 10):
	'''
	A more advanced input function. Comes with input history, initial input, and input timeout.

	### parameters
	```
	prompt: str, initInput: str = '', timeout: int = 10
	```
	`prompt:` the prompt string the user sees
	`initInput:` prefilled input text
	`timeout:` time limit for the user to respond in seconds

	### returns
	```
	response, timedOut
	``` 
	`response:` the user's response. If time limit is reached, whatever is in input buffer is returned
	`timedOut:` true or false for if the input timed out or not.

	### example
	The following will present the user with an initial option. If timed out, the next input will prefill the input with whatever was filled in from the last call
	```
	response = ''
	initial = 'red'
	timedOut = False

	while response != 'exit':
		response, timedOut = inputAdv('What is your favorite color? (5 seconds) > ', initial, 5)
		if timedOut:
			initial = response # set the prefilled input to whatever was in buffer when timed out
		else:
			initial = 'red' # reset the prefilled input
	```
	'''

	signal.signal(signal.SIGALRM, _handler)
	readline.set_startup_hook(lambda: readline.insert_text(initInput))
	signal.alarm(timeout)

	response = ''
	timedOut = False
	try:
		response = input(prompt)
	except TimeoutError:
		print('')
		response =  readline.get_line_buffer()
		timedOut = True
	except:
		print('')
	finally:
		readline.set_startup_hook(None)
	return response, timedOut


# response = ''
# initial = ''
# timedOut = False

# while response != 'exit':
# 	response, timedOut = inputAdv('5 sec > ', initial, 5)
# 	if timedOut:
# 		initial = response
# 	else:
# 		initial = ''

