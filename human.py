class Human(object):
	"""docstring for Human"""
	def __init__(self, arg):
		self.arg = arg
	def __iter__(self):
		self.a = 0
		self.b = 1
		return self
	def  __next__(self):
		fib = self.a 
		if fib > self.arg: 
			raise StopIteration 
		self.a, self.b = self.b, self.a + self.b 
		return fib

class Pow(object):
	"""docstring for Pow"""
	def __init__(self, arg,q):
		pass
		
	def test(arg,q):
		while q>0:
			arg=arg*arg
			q=q-1
		return arg