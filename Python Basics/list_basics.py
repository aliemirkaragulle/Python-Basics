# LISTS = MUTABLE SEQUENCE (ORDERED SET) OF OJECTS
my_list = [1, 2.5, "Hello", "World!", "Hello"]
print(f"ID: {id(my_list)}")



# Iterable Unpacking
obj0, obj1, obj2, obj3, obj4 = my_list
print(obj0)
print(obj1)
print(obj2)
print(obj3)
print(obj4)
print("\n")



# Sequence Indexing and Slicing

# Indexing
first_obj = my_list[0]
print(first_obj)
print(f"ID: {id(first_obj)} \n")

# Slicing
first_three_obj = my_list[0:3]
print(first_three_obj)
print(f"ID: {id(first_three_obj)} \n")



# Indexing and Slicing Assignment (In-Place Modification)

# Indexing Assignment
example_list = [1, 2, 3, 4, 5]
print(f"ID: {id(example_list)}")
example_list[0] = "CHANGED!"
print(example_list)
print(f"ID: {id(example_list)} \n")

# Slicing Assignment
example_list = [1, 2, 3, 4, 5]
print(f"ID: {id(example_list)}")
example_list[0:3] = ["CHANGED!", "CHANGED!", "CHANGED!"]
print(example_list)
print(f"ID: {id(example_list)} \n")



# Sequence Concatenation and Multiple Concatenation

# Concatenation (Not an In-Place Modification)
list0 = ["Hello"]
print(f"ID: {id(list0)}")
list0 = list0 + ["World!"]
print(list0)
print(f"ID: {id(list0)} \n")

# Concatenation Assignment (In-Place Modification)
list0 = ["Hello"]
print(f"ID: {id(list0)}")
list0 += ["World!"]
print(list0)
print(f"ID: {id(list0)} \n")

# Multiple Concatenation (Not an In-Place Modification)
list0 = ["Hello"]
print(f"ID: {id(list0)}")
list0 = list0 * 5
print(list0)
print(f"ID: {id(list0)} \n")

# Multiple Concatenation Assignment (In-Place Modification)
list0 = ["Hello"]
print(f"ID: {id(list0)}")
list0 *= 5
print(list0)
print(f"ID: {id(list0)} \n")


 
# Sequence Methods

# list.index(sub[, start[, end]])
hello_index = my_list.index("Hello")
print(hello_index)

# list.count(sub[, start[, end]])
count_hello = my_list.count("Hello")
print(count_hello, "\n")



# List Methods

# list.append(x) (In-Place Modification)
my_list = my_list = [1, 2.5, "Hello", "World!", "Hello"]
print(f"ID: {id(my_list)}")
my_list.append("Mars!")
print(my_list)
print(f"ID: {id(my_list)} \n")

# list.extend(iterable) (In-Place Modification)
my_list = my_list = [1, 2.5, "Hello", "World!", "Hello"]
print(f"ID: {id(my_list)}")
my_list.extend("STRING!")
print(my_list)
print(f"ID: {id(my_list)} \n")

# list.insert(i, x) (In-Place Modification)
my_list = my_list = [1, 2.5, "Hello", "World!", "Hello"]
print(f"ID: {id(my_list)}")
my_list.insert(1, "INSERT THIS!")
print(my_list)
print(f"ID: {id(my_list)} \n")

# list.remove(x) (In-Place Modification)
my_list = my_list = [1, 2.5, "Hello", "World!", "Hello"]
print(f"ID: {id(my_list)}")
my_list.remove("Hello")
print(my_list)
print(f"ID: {id(my_list)} \n")

# list.pop([i]) (In-Place Modification)
my_list = my_list = [1, 2.5, "Hello", "World!", "Hello"]
print(f"ID: {id(my_list)}")
pop_obj = my_list.pop()
print(pop_obj)
print(my_list)
print(f"ID: {id(my_list)} \n")

# list.sort(*, key=None, reverse=False) (In-Place Modification)
my_list = [5, 2, 14, 8, 22, 45]
my_list.sort()
print(my_list, "\n")

# list.reverse() (In-Place Modification)
my_list = [5, 2, 14, 8, 22, 45]
my_list.reverse()
print(my_list, "\n")

# list.clear()
my_list = my_list = [1, 2.5, "Hello", "World!", "Hello"]
print(f"ID: {id(my_list)}")
my_list.clear()
print(my_list)
print(f"ID: {id(my_list)} \n")



# List Comprehension
# list = [expression for item in iterable if condition == True]

list_comprehension = [num for num in range(5)]
print(list_comprehension)