"""Is-A, Has-A, Objects, and Classes."""

## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
    pass

## Dog is-a Anima and has-a __init__ that takes self and name parameters.
class Dog(Animal):

    def __init__(self, name):
        ## From self get the name attribute and set it to name.
        self.name = name

## Cat is-a Animal and has-a __init__ that takes self and name parameters.
class Cat(Animal):

    def __init__(self, name):
        ## From self get the name attribute and set it to name.
        self.name = name

## Person is-a object and has-a __init__ that takes self and name parameters.
class Person(object):

    def __init__(self, name):
        ## From self get the name attribute and set it to name.
        self.name = name

        ## Person has-a pet of some kind.
        self.pet = None

## Employee is-a Person that has-a __init__ that takes self, name, and salary parameters.
class Employee(Person):

    def __init__(self, name, salary):
        ## From Person get the __init__ that takes self and name parameters.
        super(Employee, self).__init__(name)
        ## From self get the salary attribute and set it to salary.
        self.salary = salary

## Fish is-a object.
class Fish(object):
    pass

## Salmon is-a Fish.
class Salmon(Fish):
    pass

## Halibut is-a Fish.
class Halibut(Fish):
    pass


## rover is-a Dog.
rover = Dog('Rover')

## satan is-a Cat.
satan = Cat('Satan')

## mary is-a Person.
mary = Person('Mary') 

## Mary has-a pet satan.
mary.pet = satan

## frank is-a Employee and has-a name Frank and salary 12000.
frank = Employee('Frank', 12000)

## frank has-a pet rover.
frank.pet = rover

## flipper is-a Fish.
flipper = Fish()

## crouse is-a Salmon.
crouse = Salmon()

## harry is-a Halibut.
harry = Halibut()
