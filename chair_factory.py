from abc import ABCMeta, abstractmethod, abstractstaticmethod
class IChair(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_dimensions():
        'The Chair Interface'

# we're going to create some concrete classes that
# implement that interface
class BigChair(IChair):
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80
    def get_dimensions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth }        

class MediumChair(IChair):
    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70
    def get_dimensions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth }  

class SmallChair(IChair):
    def __init__(self):
        self.height = 60
        self.width = 60
        self.depth = 60
    def get_dimensions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth }    

class ChairFactory():

    @staticmethod
    def get_chair(chairtype):
        try: 
            if chairtype == 'BigChair':
                return BigChair()
            if chairtype == 'SmallChair':
                return SmallChair()
            if chairtype == 'MediumChair':
                return MediumChair()                
            raise AssertionError('Chair no found')
        except AssertionError as _e:
            print('except is.....')
            print('_e is', _e)


if __name__ == '__main__':
    CHAIR = ChairFactory.get_chair('BigChair')   
    print('factoryMethod() method has the responsibility of creating objects of a certain type ')  
    print(CHAIR.get_dimensions())
    print(f'{CHAIR.__class__}: {CHAIR.get_dimensions()}')
    print(f'{CHAIR.__class__.__name__}: {CHAIR.get_dimensions()}')
    CHAIR = ChairFactory.get_chair('SmallChair')     
    print(CHAIR.get_dimensions())