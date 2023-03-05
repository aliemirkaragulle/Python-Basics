# DICTIONARIES = MUTABLE UNORDERED KEY:VALUE PAIRS
my_dict = {"Key1": "Value1", "Key2": "Value2", "Key3": 3, "Key4": 4.0, "Key5": [1,2,3,4,5,6]}



# Iterable Unpacking (Dictionaries Unpack Keys)

# Unpack Keys
my_dict = {"Key1": "Value1", "Key2": "Value2", "Key3": 3, "Key4": 4.0, "Key5": [1,2,3,4,5,6]}
key0, key1, key2, key3, key4 = my_dict
print(key0)
print(key1)
print(key2)
print(key3)
print(key4)
print("\n")

# Unpack Values
print(my_dict[key0])
print(my_dict[key1])
print(my_dict[key2])
print(my_dict[key3])
print(my_dict[key4])
print("\n")



# Iterable Functions 
# In Python, the built-in iterable functions operate on the keys of a dictionary when applied to a dictionary.
dict0 = {1: "HI1", 2: "HI2"}

# sum() 
print(sum(dict0))

# max()
print(max(dict0))

# min()
print(min(dict0))
print("\n")



# Operations on Dictionaries
print(my_dict)
print(f"ID: {id(my_dict)}")

# Change a Key:Value Pair (In-Place Modification)
my_dict["Key1"] = "CHANGED VALUE"
print(my_dict)
print(f"ID: {id(my_dict)}")

# Create a Key:Value Pair (In-Place Modification)
my_dict["NEW KEY"] = "NEW VALUE"
print(my_dict)
print(f"ID: {id(my_dict)}")

# Delete a Key:Value Pair (In-Place Modification)
del my_dict["NEW KEY"]
print(my_dict)
print(f"ID: {id(my_dict)} \n")



# Iteration
my_dict = {"Key1": "Value1", "Key2": "Value2", "Key3": 3, "Key4": 4.0, "Key5": [1,2,3,4,5,6]}

# Iterating Over Elements (Dictionaries Iterate Keys)
for keys in my_dict:
    print(keys)

for keys in my_dict:
    print(my_dict[keys])

# Iterating with enumerate()
for index, keys in enumerate(my_dict):
    print(index, keys)
print("\n")



# Dictionary Methods

# dict.keys() (Not an In-Place Modification)
keys = my_dict.keys()
print(keys)

for k in my_dict.keys():
    print(k)

# dict.values() (Not an In-Place Modification)
values = my_dict.values()
print(values)

for v in my_dict.values():
    print(v)

# dict.items() (Not an In-Place Modification)
items1 = my_dict.items()
print(items1)

for k, v in my_dict.items():
    print(k, v)

# dict.get(key[, value]) (Not an In-Place Modification)
value_k1 = my_dict.get("Key1")
print(value_k1)

# dict.update([mapping]) (In-Place Modification)
d = {"a": 1, "b": 2}
print(f"ID: {id(d)}")
d.update({"a": "I", "c": 3})
print(d)
print(f"ID: {id(d)}")

d = {"a": 1, "b": 2}
print(f"ID: {id(d)}")
d.update([('x', 10), ('y', 20)])
print(d)
print(f"ID: {id(d)}")

d = {"a": 1, "b": 2}
print(f"ID: {id(d)}")
d.update(foo='bar', sn='afu')
print(d)
print(f"ID: {id(d)} \n")



# Dictionary Comprehension
# my_dict = [key: value for item in iterable if condition]

dict_comprehension = {num: num**2 for num in range(1, 11)}
print(dict_comprehension)



# List of Dictionaries

# A list of dictionaries is a data structure that contains a collection of dictionaries as its elements. 
# Each dictionary in the list can store key-value pairs and can represent a separate data entity.
# In Python, lists are created using square brackets [] and dictionaries are created using curly braces {}. 
# To create a list of dictionaries, you would enclose a number of dictionaries within square brackets.

# Here's an example of a list of dictionaries:
employees = [    
    {'name': 'John Doe', 'position': 'Manager', 'salary': 50000},    
    {'name': 'Jane Doe', 'position': 'Developer', 'salary': 60000},    
    {'name': 'Jim Smith', 'position': 'Designer', 'salary': 55000}
]

# In this example, employees is a list of dictionaries, where each dictionary represents an employee. 
# Each dictionary contains three key-value pairs: 'name', 'position', and 'salary'. 
# These keys are used to store information about the employee, such as their name, job position, and salary.

# With this data structure, you can easily store and retrieve information about multiple employees. 
# For example, to retrieve the salary of the second employee, you can use the following code:

# This code would output the following: 6000
print(employees[1]['salary'])

# Notice how the for loop will iterate through each of the dicts inside the list called employees.
for employee in employees:
    print(employee["name"], employee["position"], employee["salary"], sep=", ")

# Lists of dictionaries are a versatile data structure that can be used to represent complex data sets in a organized and easily accessible way.