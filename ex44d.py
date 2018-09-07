"""Inheritance vs. Composition."""

class Parent(object):
	def override(self):
		print('PARENT override()')

	def implicit(self):
		print('PARENT implicit()')

	def altered(self):
		print('PARENT altered()')


class Child(Parent):
	def override(self):
		print('CHILD override()')

	def altered(self):
		print('CHILD BEFORE altered()')
		super(Child, self).altered()
		print('CHILD AFTER altered()')


def main():
	dad = Parent()
	son = Child()

	dad.override()
	son.override()

	dad.implicit()
	son.implicit()

	dad.altered()
	son.altered()


if __name__ == '__main__':
	main()
