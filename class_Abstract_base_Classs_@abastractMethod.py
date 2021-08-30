# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod 

class Shape(ABC):
# class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(Shape):
    type ="Rectangle"
    side = 4
    def __init__(self):
        self.length = 6
        self.breath = 7

    def printArea(self):
        return self.length * self.breath


rect1 = Rectangle()   
print(rect1.printArea())                   