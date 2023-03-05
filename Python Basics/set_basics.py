# SETS = MUTABLE UNORDERED COLLECTION OF UNIQUE OBJECTS
my_set = {1, 2, 5}

# Empty Set
zero = set()
print(f"TYPE: {type((zero))}, {zero}")

# Single Element Set
one = {"Hello"}
print(f"TYPE: {type((one))}, {one}")
print("\n")



# Iterable Unpacking 
obj0, obj1, obj2 = my_set
print(obj0)
print(obj1)
print(obj2)
print("\n")



# Iterable Functions 

# sum() 
print(sum(my_set))

# max()
print(max(my_set))

# min()
print(min(my_set))
print("\n")



# Operations on Sets
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 3, 5, 7, 9}
print(f"Set A: {a}")
print(f"Set B: {b}")

# Objects in A
print(f"A: {a}")

# Objects in A but Not in B (Not an In-Place Modification)
# A \ B = {x | x ∈ A and x ∉ B}
print(f"A Intersection B': {a - b}")

# Objects in A or B or Both (Not an In-Place Modification)
# A ∪ B {x | x ∈ A or x ∈ B}
print(f"A Union B: {a | b}")

# Objects in Both A and B (Not an In-Place Modification)
# A ∩ B = {x | x ∈ A and x ∈ B}
print(f"A Intersection B: {a & b}")

# Objects in A or B but Not Both (Not an In-Place Modification)
# A ^ B = (A - B) ∪ (B - A) = {x | x ∈ A and x ∉ B} ∪ {x | x ∈ B and x ∉ A}
print(f"A Intersection B' Union B Intersection A': {a ^ b} \n")



# Set Methods

# set.add(element) (In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
my_set.add(10)
print(my_set)
print(f"ID: {id(my_set)} \n")

# set.update(other, …) (In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
my_set.update({3, 4}, [12, 14])
print(my_set)
print(f"ID: {id(my_set)} \n")
    
# set.discard(element) (In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
my_set.discard(1)
print(my_set)
print(f"ID: {id(my_set)} \n")

# set.difference(iterable, …) (Not an In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
set_difference = my_set.difference({1, 2, 3, 4})
print(set_difference)
print(f"ID: {id(set_difference)} \n")
    
# set.intersection(iterable, …) (Not an In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
set_intersection = my_set.intersection({1, 2, 3, 4})
print(set_intersection)
print(f"ID: {id(set_intersection)} \n")
    
# set.symmetric_difference(iterable) (Not an In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
set_symm_diff = my_set.symmetric_difference({1, 2, 3, 4})
print(set_symm_diff)
print(f"ID: {id(set_symm_diff)} \n")

# set.union(iterable, …) (Not an In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
set_union = my_set.union({1, 2, 3, 4})
print(set_union)
print(f"ID: {id(set_union)} \n")

# set.difference_update(iterable, …) (In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
my_set.difference_update({1, 2, 3, 4})
print(my_set)
print(f"ID: {id(my_set)} \n")
    
# set.intersection_update(iterable, …) (In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
my_set.intersection_update({1, 2, 3, 4})
print(my_set)
print(f"ID: {id(my_set)} \n")
    
# set.symmetric_difference_update(iterable) (In-Place Modification)
my_set = {1, 2, 5}
print(my_set)
print(f"ID: {id(my_set)}")
my_set.symmetric_difference_update({1, 2, 3, 4})
print(my_set)
print(f"ID: {id(my_set)} \n")



# Set Comprehension
# set = {expression for item in iterable if condition == True}
set_comprehension = {num for num in range(10)}
print(set_comprehension)
print("\n")



# When you convert a list to a set, it will only retain the unique elements in the list, discarding any duplicates.
my_list = [1, 1, 1, 1, 2, 2, 2, 2]
print(my_list)
my_list = list(set(my_list))
print(my_list)