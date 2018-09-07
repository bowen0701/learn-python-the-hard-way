"""Inheritance vs. Composition."""

class Parent(object):
	def override(self):
		print('PARENT override()')


class Child(Parent):
	def override(self):
		print('Child override()')


def main():
	dad = Parent()
	son = Child()

	dad.override()
	son.override()

if __name__ == '__main__':
	main()
