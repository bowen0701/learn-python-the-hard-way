"""Inheritance vs. Composition."""

class Parent(object):
	def altered(self):
		print("PARENT altered()")


class Child(Parent):
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")


def main():
	dad = Parent()
	son = Child()

	dad.altered()
	son.altered()

if __name__ == '__main__':
	main()
