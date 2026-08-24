from abc import ABC, abstractmethod
# ABC → Base class for abstract classes
# @abstractmethod → Defines a method that must be implemented
# by child classes
# abstract methods are implemented in child class not in their own class 
# Python provides abstraction using the abc module.
class Animal(ABC):  # abstract class
    # the function(abstract method) will not implementr in abstract class 
    # it will implement in child class
    # here we are hiding implementation of abstract method in abstract class
    @abstractmethod
    def make_sound():
        pass


class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")


lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()