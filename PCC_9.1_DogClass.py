# This class will serve as a blueprint for real world objects(dogs) - class, attribute, & instantation example

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 9, example 1+
    # Made with Mu 1.0.3 in November 2021

class Dog():                                    # create dog class
    """A blueprint for a typical dog"""
    
    def __init__(self, name, age):              # create a method = a function that is part of a class
        """name and age attributes"""                        
        self.name = name                        # attribute = variables accesible from instances
        self.age = age
        
    def sit(self):                              # sit method
        """method - sit"""
        print(self.name.title() + " has sat down")
        
    def roll_over(self):                        # roll over method
        """method - roll over"""
        print(self.name.title() + " has rolled over")
        
my_dog = Dog('george', 6)                       # instantation = making a specific object(dog) from a class

print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old")

my_dog.sit()                                    # call the sit method
my_dog.roll_over()
