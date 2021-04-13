# Learn how to create simple factory which helps to hide logic of creating objects.
from abc import ABCMeta, abstractmethod

class AbstractDegree(metaclass=ABCMeta): # is an abstract concrete class
    @abstractmethod
    def info(self):
        pass 
class BE(AbstractDegree): # is concrete class
    def info(self):
        print('Bachelor of engineering')    
    def __str__(self):
        return 'Bachelor of engineering'                
class ME(AbstractDegree): # is concrete class
    def info(self):
        print('Master of engineering')        
    def __str__(self):
        return 'Master of engineering'
class MBA(AbstractDegree): # is concrete class 
    def info(self):
        print('Master of business administration')        
    def __str__(self):
        return 'Master of business administration'

class ProfileAbstractFactory(object): # is an abstract factory
    def __init__(self):
        self._degrees = []
    # which has one declared method createProfile
    # which must be implemented by individual profile factory
    @abstractmethod
    def createProfile(self):
        pass 
    def addDegree(self, degree): # instance method to help creating profile of different designations.

        self._degrees.append(degree)
    def getDegrees(self):
        return self._degrees 

# EngineerFactory, ManagerFactory are factories which has implemented
# createProfile method as both can have different degrees.         
class ManagerFactory(ProfileAbstractFactory): # is a Factory which has implemented createProfile method

    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(MBA())
        return self._degrees

class EngineerFactory(ProfileAbstractFactory): # is a Factory w
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(ME())
        return self._degrees

# Now ProfileFactory, final factory which creates profile which you want by passing
# instance of EngineerFactory or other related.
class ProfileFactory(object):
    def getProfile(self, factory):
        return factory.createProfile()

    

if __name__ == "__main__":
    pf = ProfileFactory().getProfile(ManagerFactory())
    print(pf)        