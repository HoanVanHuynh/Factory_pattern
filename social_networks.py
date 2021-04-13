from abc import ABCMeta, abstractmethod, abstractstaticmethod

# Let's now take a look at the implementation.
# In the following code example,
# we will start by defining the Product interface.

# We will create a Section abstract class that defines how a section will be.
# we will keep it very simple and provide an abstract method, describe()

class Section(metaclass=ABCMeta): # Product interface
    @abstractmethod
    def	describe(self): # abstract method
        pass
# We now create multiple ConcreteProduct classes 
# These classes implement the describe() abstract method
# and print their respective section names: 
#  
class PersonalSection(Section): # ConcreteProduct
    def	describe(self):
        print("Personal	Section")
class AlbumSection(Section): # ConcreteProduct
    def	describe(self):
        print("Album	Section")
class PatentSection(Section): # ConcreteProduct
    def	describe(self):
        print("Patent	Section")
class PublicationSection(Section): # ConcreteProduct
    def	describe(self):
        print("Publication	Section")

# We create a Creator abstract class that is named Profile.
# The Profile [Creator] abstract class provides a factory method, createProfile()
# The createProfile() method should be implemented by ConcreteClass 
#  to actually create the profiles with appropriate sections.      
#
class Profile(metaclass=ABCMeta): # Creator 
    def __init__(self):
        self.sections = []
        self.createProfile()   

    @abstractmethod
    def createProfile(self): # factory method
        pass
    def getSections(self):
        return self.sections
    def addSections(self, section):
        self.sections.append(section)
# we create two ConcreteCreator clases, linkedin and facebook.
# Each of these classes implement the createProfile() abstract method
# that actually creates (instantiates) multiple sections (ConcreteProducts) at runtime: 

class linkedin(Profile): # ConcreteCreator
    def createProfile(self): # overrides the factory method
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class facebook(Profile): # ConcreteCreator
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

# We finally write client code that determines which Creator class to instantiate
# in order to create a profile of the desired choice:
if __name__ == '__main__':
    profile_type = input('Which Profile you would like to create? [LinkedIn or FaceBook]')
    print(eval(profile_type))
    print(eval(profile_type.lower()))
    profile = eval(profile_type.lower())()
    print(profile)
    print('Creating Profile..', type(profile).__name__) 
    print('Profile has sections --', profile.getSections())
# If you now run the complete code, it'll first ask you 
# to enter the name of the profile that you'd like to create.
# In the following screenshot, we say Facebook.
# It then instantiates the facebook [ConcreateCreator] class.
# This internally creates ConcreteProduct(s), that is, 
# it instantiates PersonalSection and AlbumSection.
# If Linkedin is chosen, then PersonalSection, PatentSection, and PublicationSection are created.     