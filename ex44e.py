"""Inheritance vs. Composition."""

class Other(object):
	def implicit(self):
		print('OTHER implicit()')

	def override(self):
		print('OTHER override()')

	def altered(self):
		print('OTHER altered()')


class Child(object):
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print('CHILD override()')

	def altered(self):
		print('CHILD BEFORE altered()')
		self.other.altered()
		print('CHILD AFTER altered()')


def main():
	son = Child()

	son.implicit()
	son.override()
	son.altered()


if __name__ == '__main__':
	main()
