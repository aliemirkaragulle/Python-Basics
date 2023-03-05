# PYTHON BASICS

# Python is a high level, interpreted, interactive, dynamically-typed, garbage-collected, object oriented, general purpose script language.
# All the data in a Python code is represented by objects or by relations between objects.



# OBJECTS
obj_01 = 5
obj_02 = 5.0
print(obj_01)
print(obj_02, "\n")

# Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects. Every Object has an identity, a type, and a value. 
# Objects are values stored in memory that are referenced by identifiers and contain other values.
# An Object is an instance of a Class.
# Every object has an identity, a type, and a value.

# Identity
# Identity is an object's address in memory.
# Identity of an object never changes once created. 
# id() function returns an integer representing an object's identity.
# is operator compares the identity of two objects.
print(f"ID of the Object obj_01: {id(obj_01)}")
print(f"ID of the Object obj_02: {id(obj_02)}")

# It should be noted that equality is not identity!
print(f"Are the Objects Equal? {obj_01 == obj_02}")
print(f"Are the Object Identical? {obj_01 is obj_02}")
print("\n")

# Type
# Data types are classifications of values that determine the set of operations that can be performed on those values and the way the values are stored in memory. 
# Type of an object never changes.
# type() function returns the type of an object.
print(f"Type of the Object obj_01: {type(obj_01)}")
print(f"Type of the Object obj_02: {type(obj_02)}")
print("\n")

# Value
# In Python, a value is a basic unit of data that represents a piece of information, and belongs to a specific data type.
# The value of some objects can change.
# Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable.
# An object’s mutability is determined by its type.
mutable_obj = ["Lists are Mutable!"]
immutable_obj = "Strings are Immutable!"

def mutable_immutable(obj):
    try:
        obj[0] = "Changed!"
        return f"{type(obj)} is Mutable!"
    except:
        return f"{type(obj)} is Immutable!"

print(mutable_immutable(mutable_obj))
print(mutable_immutable(immutable_obj))
print("\n")



# VARIABLES 
# Variables are references to Objects. A Python variable is a named reference to a value stored in memory.
# In Python, variables are dynamically typed, which means that the type of a variable is determined by the value that is assigned to it, 
# and the variable can hold references to values of different types at different times. 
# Another characteristic of Python variables is that they can be reassigned to refer to different values at any time.
# Variables never point to other variables.

# A variable never truly "contains" a value, in the same way as a container does not really "contain" values.
# All they contain are references (the arrows).
# When you "change the value" of a variable, you are actually changing the reference.

# The key idea is that objects and variables have their own existence.



# MUTABLE & IMMUTABLE OBJECTS
# Mutable objects are objects that can be modified after creation, while immutable objects are objects that cannot be modified after creation. 
# The mutability of an object is determined by its type, with some types being mutable and others being immutable.

# In Python, variables that reference immutable objects will always point to the same object if they are assigned the same value, 
# while variables that reference mutable objects will point to different objects even if they are assigned the same value.
# This is because immutable objects cannot be modified, so creating a new variable and assigning it the same value as an 
# existing immutable object simply creates a new reference to the same object, while mutable objects can be modified,
# so creating a new variable and assigning it the same value as an existing mutable object creates a new object with the same contents as the original.
imm_obj_01 = "Strings are immutable objects!"
imm_obj_02 = "Strings are immutable objects!"
print(f"ID of the Object imm_obj_01: {id(imm_obj_01)}")
print(f"ID of the Object imm_obj_02: {id(imm_obj_02)}")
print(imm_obj_01 is imm_obj_02)
print("\n")

mut_obj_01 = [1,2,3]
mut_obj_02 = [1,2,3]
print(f"ID of the Object mut_obj_01: {id(mut_obj_01)}")
print(f"ID of the Object mut_obj_02: {id(mut_obj_02)}")
print(mut_obj_01 is mut_obj_02)
print("\n")

# When two variables reference to the same mutable object and that object is mutated, both variables are affected. 
# However, for immutable objects, this is not true.
mut_ref = mut_obj_01
mut_obj_01[0] = "Changed!"
print(mut_obj_01)
print(mut_ref)
print("\n")

imm_ref = imm_obj_01
imm_obj_01 = "New Object!"
print(imm_obj_01)
print(imm_ref)
print("\n")

# In-place Modification
# In-place modification is the process of directly modifying a mutable object, rather than
# creating a new object as a result of the modification, and it is not possible for immutable objects.
l = [1, 2, 3, 0, -2, -4]
print(f"ID of l: {id(l)}")
# foo += bar is an in-place operation. 
l += [5]
print(f"ID of l after foo += bar: {id(l)}")
# foo = foo + bar is not an in-place operation.
l = l + [5]
print(f"ID of l after foo = foo + bar: {id(l)}")