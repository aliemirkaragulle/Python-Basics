# OBJECT ORIENTED PROGRAMMING (OOP)
# Object-oriented programming (OOP) is a programming paradigm that uses objects and their interactions to design applications and computer programs. 
# In Python, OOP concepts include classes, objects, inheritance, polymorphism, and encapsulation.

# OOP allows programmers to create their own objects that have attributes and methods.



# Classes
# Classes are user-defined objects in Python. A class is a blueprint for creating objects, and it defines the attributes and methods that the objects will have.
# Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

# Syntax of a Class:
"""
class NameOfClass():
    
    def__init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    
    (def__init__(self, param1, param2):
        self.attribute = param1
        self.attribute = param2)

    def some_method(self):
        # perform some action
        print(self.param1)
"""
class Dog:
    def __init__(self, name, breed):
        print("A Dog is created!")
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# Attributes: "name" and "breed" are attributes of the Dog class. They are defined inside the class and describe the state of the Dog object.
# Methods: "bark" is a method of the Dog class. It is defined inside the class and can be called on a Dog object to make it "bark".

# class keyword
# The class keyword is a reserved word in Python that is used to define a new class. It is followed by the name of the class, and a colon. 
# The class definition is the blueprint for creating objects, and it defines the attributes and methods that the objects will have.

# From classes, we can construct instances. 



# Instance
# An instance is an individual occurrence of an object that is created from a class. 
# An instance is a specific realization of a class, and it has its own state, which is represented by the values of its attributes.

# When you create an object using the class definition, that object is referred to as an instance of the class. 
# For example,
dog1 = Dog("Fido", "Golden Retriever")
dog2 = Dog("Buddy", "Beagle")

# Here, dog1 and dog2 are instances of the class Dog. They have their own unique state, represented by their name and breed attributes.
# Each instance has a separate memory allocation, so changes to the attributes of one instance does not affect the attributes of another instance.

# In summary, an instance is a specific realization of a class, created by instantiating the class, 
# it has its own state represented by the attributes and can have its own behavior represented by the methods.

# An instance is a specific object created from a particular class.
# my_list = [1, 2, 3, 4]
# my_list is an instance of a list object.



# Instantiation
# "Instantiation" is the process of creating an instance of a class. It is the process of creating an object from a class definition. 
# When a class is instantiated, memory is allocated for the object, and the constructor method (if defined) is called to initialize the object's attributes.
# For example,
dog1 = Dog("Fido", "Golden Retriever")

# Here, dog1 is an instance of the class Dog and it's instantiated by calling the class Dog and passing the arguments "Fido" 
# and "Golden Retriever" to the constructor method __init__ which creates the object and initializes its attributes.

# In summary, instantiation is the process of creating an instance of a class, allocating memory for the object, and initializing its attributes by calling the constructor method.

# Example)
# Create a new object type called Sample
class Sample:
    pass

# Create an instance of Sample
x = Sample() 
print(type(x))
print("\n")

# Note how x is now an instance of the Sample class.
# In other words, we instantiated the Sample class.

# In summary, this code creates a class called Sample, and then it creates an instance of that class, 
# which is an object of that class, and assigns it to the variable x. The type of x is confirmed to be of Sample.



# Attributes and Methods

# Attributes
# An attribute is a property or a characteristic of an object that describes its state. 
# In object-oriented programming, an attribute refers to a variable that is defined within a class and represents some aspect of the object that is an instance of that class.
# Attributes can also be defined outside of the class, but they will belong to the instance of the class and not the class itself.
# In summary, attributes are variables that store data within an object and describe the state of the object.

# Each attribute in a class definition begins with a reference to the instance object. It is, by convention, named self.
# The syntax <self.attribute_name = parameter> is the correct way of assigning attributes inside the constructor method in Python.

# In Python, attributes can be classified into two types:

# Instance attributes: 
# These are attributes that are specific to an instance of a class. They are defined inside the constructor method __init__ and are unique for each instance of the class. 
# For example, in the previous example, "name" and "breed" are instance attributes of the Dog class, they are defined inside the class and describe the state of the Dog object.

# Class attributes: 
# These are attributes that are shared among all instances of a class. They are defined outside the constructor method and are the same for all instances of the class. 
# For example, if all the instances of a class has the same color, you can define it as a class attribute.
class Dog:
    color = "brown"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Here, color is a class attribute, all instances of the Dog class will have "brown" as the color.
# It's important to note that instance attributes have priority over class attributes, 
# if an instance attribute has the same name as a class attribute, the instance attribute will be used when accessed.

# In summary, attributes in Python can be classified into two types: 
# instance attributes, which are specific to an instance of a class, and class attributes, which are shared among all instances of a class.

# In Python, you can access instance attributes and class attributes inside the class definition using the self and classname respectively.

# To access an instance attribute inside the class definition, you use the self parameter followed by the attribute name. 
#  For example, in the following class definition, the __init__ method assigns the value of the name parameter 
# to the name attribute of the current instance of the class using the self.name = name syntax:
"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
"""

# To access a class attribute inside the class definition, you use the name of the class followed by the attribute name. 
# For example, in the following class definition, the get_color method returns the value of the color attribute of the class using the Dog.color syntax:
"""
class Dog:
    color = "brown"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def get_color(self):
        return Dog.color
"""

# It is important to note that when you access class attributes inside class methods, you have to use the class name and not the self parameter, 
# otherwise Python will treat it as an instance attribute.

# In summary, instance attributes can be accessed inside the class definition using the self parameter followed by the attribute name, 
# and class attributes can be accessed inside the class definition using the name of the class followed by the attribute name.



# __init__ (Constructor Method) 
# __init__ is a special method in Python classes, it is a constructor method, that is automatically called when an object of the class is created. 
# The __init__ method is used to initialize the object's attributes, and it is defined inside a class definition.

# The __init__ method has the following syntax:
"""
def __init__(self, parameters):
    # Initialization code here
"""

# The parameters are the values passed to the constructor method when the object is created, they are used to set the initial state of the object's attributes.
# For example:
"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
"""
# Here, __init__ method takes two parameters name and breed which are used to initialize the name and breed attributes of the object.
# It is important to note that when the class is instantiated, the __init__ method is called automatically, so you don't need to call it explicitly.

# In summary, __init__ is a special method in Python classes, it is a constructor method, which is automatically called when an object of the class is created. 
# It is used to initialize the object's attributes and set the initial state of the object.



# self 
# The self parameter in Python classes is a reference to the current instance of the class. 
# It is used to access the attributes and methods of the object. 
# The self parameter is passed automatically to the class methods when they are called, and it is the first argument of a class method.

# When you call a method on an object, Python automatically passes the object as the first argument to the method. This argument is usually named self by convention.
# For example:
"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")
"""

# Here, self is the first argument of both methods __init__ and bark. 
# It is used to access the object's attributes name and breed in the constructor and to execute the method bark on the object.

# It is important to note that the self parameter is not a keyword, it's a naming convention, you can use any name, but the convention is to use self.

# In summary, the self parameter in Python classes is a reference to the current instance of the class, 
# it is passed automatically to class methods when they are called and it is used to access the attributes and methods of the object.



# Methods
# A method is a function that is defined within a class and is used to perform actions on or with the object that is an instance of that class.
# In object-oriented programming, a method is a function that is associated with an object and operates on the data within that object. 
# Methods are defined within a class, and can be called on an instance of that class, allowing the object to perform some action or computation.
# A method generally take self as the first parameter which refers to the instance of the class, but this is not always the case.
# In summary, methods are functions that are associated with an object and operate on the data within that object to perform some action or computation.

# Methods act as functions that use information about the object, as well as the object itself to return results, or change the current object.

# Methods arer functions defined inside the body of a class. They are used to perform operations with the attributes of our objects.
# You can basically think of methods as functions acting on an object tjat take the object itself into account through its self argument.



# Example)
class Circle:
    # Class Object Attribute
    pi = 3.14

    """
    The __init__ method runs automatically when an object of a class is created, it is called automatically by Python when the class is instantiated, 
    and it is used to initialize the object's attributes and set the initial state of the object.
    """
    # "The Circle class is instantiated with an optional radius argument, with a default value of 1, representing the size of the circle's instance."
    def __init__(self, radius = 1):
        # Instance Attribute
        self.radius = radius
        self. area = radius * radius * Circle.pi

    # Method for re-setting the radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * Circle.pi

    # Method for getting the circumference
    def getCircumference(self):
        return self.radius * self.pi * 2

# c is an Instance of the Circle class
# The Circle class is instantiated
# An instance of the Circle class is instantiated with the default radius of 1
c = Circle()

print(c.radius)
print(c.area)
print(c.getCircumference())
print("\n")

c.setRadius(2)
print(c.radius)
print(c.area)
print(c.getCircumference())
print("\n")



# Inheritance
# Inheritance is a mechanism in object-oriented programming. 
# It allows one class (the subclass or derived class) to inherit attributes and methods from another class (the superclass or base class). 
# The subclass inherits the attributes and methods of the superclass and can also add new attributes and methods or override existing ones.

# Inheritance is a way to form new classes using the classes that have already been defined.
# The newly formed classes are called derived classes (or subclass), the classes that we derive from are called base classes (or superclass).
# The derived classes (descendants) override or extend the functionality of base classes (ancestors).
# Inheritance allows for code reusability, you can use the attributes and methods of the superclass in the subclass without having to define them again. 
# It also allows for easier maintenance of the code, you can make changes to the superclass and have those changes automatically reflected in all subclasses.

# In summary, Inheritance is a mechanism in object-oriented programming that allows one class to inherit attributes and methods from another class. 
# It allows for code reusability and easier maintenance of the code.

# In this example, we have two classes. Animal and Dog.
# The Animal is the base class, and the Dog is the derived class.

# The derived class inherits the functionality of the base class (eat method).
# The derived class modifies the existing behaviour of the base class (whoAmI method).
# The derived class extends the functionality of the base class (bark method).

# Base Class (Super-class)
class Animal:
    def __init__(self):
        print("Animal created!")
    
    def whoAmI(self):
        print("Animall")
    
    def eat(self):
        print("I am eating.")

# Derived Class (Sub-class)
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created!")
    
    def whoAmI(self):
        print("Dog")
    
    def bark(self):
        print("Woof")

d = Dog()
print("\n")

d.whoAmI()
d.eat()
d.bark()
print("\n")

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def human(self):
        print("I am a human!")

class Worker(People):
    def __init__(self, name, age, wage):
        super().__init__(name, age)
        self.wage = wage
    
    def human(self):
        print("I am a human. I am working!")

d = Worker("Joe", 35, 1500)
print(d.name)
print(d.age)
print(d.wage)

d.human()
print("\n")



# Polymorphism
# Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. 
# It allows objects of different classes to be used interchangeably, and it enables the use of a single interface to represent multiple types of objects.

# In Python, Polymorphism refers to the way in which different object classes can share the same method name, 
# and those methods can be called from the same place even though a variety of different objects might be passed in.
# A more common practice is to use abbstract classes and Inheritance.
# An abstract class is one that never expects to be instantiated. 

# For example, we'll never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:
class Animal:
    # Constructorr of the class
    def __init__(self, name):
        self.name = name

    # Abstract method (Convention)
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return self.name + " SAYS WOOF!"

class Cat(Animal):
    def speak(self):
        return self.name + " SAYS MEOW!"

fido = Dog("Fido")
isis = Cat("Isis")

# Here we have a Dog class and a Cat class and each has a .speak() method.
# When called, each object's .speak() method returns a result unique to the object.

# There are different ways to demonstrate Polymorphism.
# First, with a for loop, and another is with functions.
# In both cases, we were able to pass in different object types, and we obtained object-specific results from the same mechanism.
print(fido.speak())
print(isis.speak())
print("\n")

for pet in [fido, isis]:
    print(pet.speak())
print("\n")

def pet_speak(pet):
    print(pet.speak())

pet_speak(fido)
pet_speak(isis)
print("\n")



# Special Methods
# In Python, special methods are methods that have double underscores at the beginning and end of their names (e.g. __init__, __str__). 
# These methods are used to define the behavior of objects and classes in special situations, such as when an object is created, when it's printed, or when it's compared to other objects.

# Special methods are also known as "magic methods" or "dunder methods" (short for "double underscore"). 
# They are not meant to be called directly by the user, but rather they are called by the Python interpreter in certain situations.

# Here are some of the must-known special methods in Python:
# str(p) -> gets translated into p.__str__()
# (Use __repr__! It must always return a string. Iterables print(), str(), etc.)

# len(p) -> gets translated into p.__len__()

# p == r gets translated into __eq__(self, other)
# (Must return a bool! Without __eq__, == will checck identity!)

# p[k] gets translated into __getitem__(self, key)

# p[k] = v gets translated into __setitem__(self, k, v)
# (Do not use a return statement! self[k] = v)

# p < r gets translated into __lt__(self, other)

# p <= r gets translated into __le__(self, other)

# __add__(self, other) addition p + r (p is the self and r is the other)
# __sub__(self, other) subtraction p - r (p is the self and r is the other)
# __mul__(self, other) multiplication p * r (p is the self and r is the other)
# __truediv__(self, other) division p / r (p is the self and r is the other)
# __floordiv__(self, other) floor (integer) division p // r (p is the self and r is the other)
# (In general, are returned to instantiate a new instance of the class.)
"""
class Point:
    # __init__ method here

    # def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
"""

# "All arithmetic operators have corresponding in-place methods associated; for example, __iadd__ for +, __isub__ for -, and so on.""""
""" 
def __iadd__(self, other):
    self.x += other.x
    self.y += other.y
"""

# "__int__(self) converts the object to an integer.
#  __float__(self) converts the object to a float. 
# __call__ allows an object to be callable, like a function. "

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Title: {self.title}, Author = {self.author}, Number of Pages = {self.pages}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed!")

book = Book("Crime and Punishment", "Dostoyevski", 500)

# Special Methods
print(book)
print(len(book))
del book
print("\n")