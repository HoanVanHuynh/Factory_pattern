# pylint: disable=too-few-public-methods
"The Factory Concept"
from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    "A Hypothetical Class Interface (Product)"

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"
    

class ConcreteProductA(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"

    def __repr__(self):
        return f'This is a product{self.name}'
    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self

class ConcreteProductC(IProduct): # The ConcreteCreator class
    "A Concrete Class that implements the IProduct interface"

    # has factoryMethod() that implements the Creator abstract class 
    
    def __init__(self):
        self.name = "ConcreteProductC"

    # this method can change the created object at runtime 
    def create_object(self):
        return self

class Creator: # We have an absstract class, Creator,
    # that contains factoryMethod()
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        # The factoryMethod() method 
        # has the responsibility of creating objects of a certain type.
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None

# The Client
PRODUCT = Creator().create_object('b')
print(PRODUCT.name)