# TUPLES = IMMUTABLE SEQUENCE (ORDERED SET) OF OBJECTS
my_tuple = "This is a tuple!", 55, 666, 5.5, "Hello"

# Empty Tuple
zero = ()
print(zero)

# Single Element Tuple
singleton = ("Hello",)
print(singleton)
print("\n")



# Iterable Unpacking
obj0, obj1, obj2, obj3, obj4  = my_tuple
print(obj0)
print(obj1)
print(obj2)
print(obj3)
print(obj4)
print("\n")



# Sequence Indexing and Slicing

# Indexing
first_obj = my_tuple[0]
print(first_obj)

# Slicing
first_three_obj = my_tuple[0:3]
print(first_three_obj)
print("\n")


 
# Sequence Concatenation and Multiple Concatenation (Not an In-Place Modification Since Tuples are Immutable)

# Concatenation 
tup = (1, 2, 3)
new_tup = (2,) + tup[1:] 
print(new_tup)

tup = ("Hello",)
tup = tup + ("World!",)
print(tup)

# Concatenation Assignment
tup = ("Hello",)
tup += ("World!",)
print(tup)

# Multiple Concatenation (Not an In-Place Modification)
tup = ("Hello",)
tup = tup * 5
print(tup)

# Multiple Concatenation Assignment (In-Place Modification)
tup = ("Hello",)
tup *= 5
print(tup)
print("\n")



# Sequence Methods

# tuple.index(sub[, start[, end]])
hello_index = my_tuple.index("Hello")
print(hello_index)

# tuple.count(sub[, start[, end]])
count_hello = my_tuple.count("Hello")
print(count_hello)