


class test():
	def __init__(self) -> None:
		self.attr = ' abc'



class change():
	def __init__(self, var: test) -> None:
		self.a = var
		self.a.attr = 'bbbb'



a = test()

print(a.attr)


b = change(a)


print(a.attr)

