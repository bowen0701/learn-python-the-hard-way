"""Inheritance vs. Composition."""

class Parent(object):
    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass


def main():
    dad = Parent()
    son = Child()

    dad.implicit()
    son.implicit()

if __name__ == '__main__':
    main()
