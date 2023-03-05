# FUNCTIONS AND METHODS

# Functions
# In Python, a function is a block of reusable code that takes input parameters, performs a specific task and returns a value or output.
# The keyword "def" introduces a function definition.
# In Python, the syntax for defining a function is as follows:
"""
def function_name(parameters):
    # function body
    # statements
    return [expression]

The keyword def is used to indicate the start of a function definition.
The function_name is the name of the function, which should be a descriptive name and usually start with a lowercase letter. It should not be a keyword.
The parameters are a comma-separated list of variables that are passed as inputs to the function. The parameters are enclosed in parentheses (). If there are no parameters, the parentheses should be left empty.
The function body is indented and contains the statements that are executed when the function is called.
The return statement is used to return a value from the function. If a function does not have a return statement, it will return None by default.
"""
def add(a, b):
    return a + b

result = add(3,4)
print(result) # Prints 7
print("\n")
# It's worth noting that, in Python, function arguments can be passed by position or by keyword, and function can also have default values for some or all arguments.



# Function Arguments
# In Python, function arguments can be passed in two ways: by position and by keyword.

# When passing arguments by position, the order of the arguments matters. 
# The interpreter will match the first argument to the first parameter, the second argument to the second parameter, and so on. For example:
def my_function(a, b):
    return a + b

result = my_function(1, 2)

# In this example, the value 1 is passed as the first argument and it is matched with the first parameter a, 
# and the value 2 is passed as the second argument and it is matched with the second parameter b.

# When passing arguments by keyword, the order of the arguments does not matter. 
# The interpreter will match the argument to the parameter with the corresponding keyword. For example:
def my_function(a, b):
    return a + b

result = my_function(b=1, a=2)

# In this example, the values are passed by keyword, and the order of the arguments does not matter. 
# The value 1 is passed as the argument for b and it is matched with the parameter b, and the value 2 is passed as the argument for a and it is matched with the parameter a.

# Additionally, Python functions can also have default values for some or all arguments. 
# These default values are used if the corresponding argument is not passed in the function call. For example:
def my_function(a, b=0):
    return a + b

result = my_function(1)

# In this example, the function my_function has a default value of 0 for the parameter b. 
# In this call, the value 1 is passed for a, and the default value 0 is used for b, so the result will be 1 + 0 = 1.

# RULE: 
# When defining a function in Python, the positional arguments must be placed before the named arguments in the parameter list, 
# and when calling the function, the positional arguments must be specified before the named arguments.

# return statement
# In Python, the "return" statement is used inside a function to exit the function and return a value or output to the place where the function was called. 
# The return statement can be used without any value or with a value or expression. 
# When a return statement is executed, the function stops executing, and the value or expression following the return statement is returned to the caller.



# Methods
# A method is a function that is associated with an object. It is used to perform an action on or with the object.



# *args

# In Python, *args is a way to pass a variable number of arguments to a function. 
# It is used as a parameter in a function definition, and it allows a function to accept any number of arguments passed to it.
# When a function is defined with *args as a parameter, any number of arguments passed to the function will be collected and stored in a tuple named args.

# For example, the following function takes any number of arguments and prints them out:
def print_args(*args):
    for arg in args:
        print(arg)

# You can call the function passing any number of arguments:
print_args(1,2,3)
print("\n")
print_args("a", "b", "c")
print("\n")

# It's important to note that the * symbol is used to pass variable arguments, not keyword arguments. To pass variable keyword arguments, you use **kwargs.



# **kwargs

# In Python, **kwargs is a way to pass a variable number of keyword arguments to a function. 
# It is used as a parameter in a function definition, and it allows a function to accept any number of keyword arguments passed to it.
# When a function is defined with **kwargs as a parameter, any number of keyword arguments passed to the function will be collected and stored in a dictionary named kwargs.

# For example, the following function takes any number of keyword arguments and prints them out:
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# You can call the function passing any number of keyword arguments:
print_kwargs(Name="John", Age=25)
print_kwargs(City="New York", Country="USA")
print("\n")

def myfunc(**kwargs):
    if 'Fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['Fruit']}!")  
    else:
        print("I don't like fruit")
        
myfunc(Fruit = "pineapple")
myfunc()
print("\n")



# *args and **kwargs 

# You can pass *args and **kwargs into the same function, but *args have to appear before **kwargs
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass

myfunc('eggs','spam',fruit='cherries',juice='orange')
print("\n")

# Placing keyworded arguments ahead of positional arguments raises an exception:
# myfunc(fruit='cherries',juice='orange','eggs','spam')

# As with "args", you can use any name you'd like for keyworded arguments - "kwargs" is just a popular convention.



# map(function, iterable, *iterables)
# Return an iterator that applies function to every item of iterable, yielding the results.
# If additional iterables arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.

def square_nums(num):
    return num ** 2
nums = [1, 2, 3, 4]
# To get the results, either iterate through map() or cast to a list.
print(list(map(square_nums, nums)))
print("\n")

print(list(map(lambda x: x**3, nums)))
print("\n")

print(list(map(lambda x, y: x * y, nums, [2, 5, 10, 20])))
print("\n")


# filter(function, iterable)
# Construct an iterator from those elements of iterable for which function returns True. 
# iterable may be either a sequence, a container which supports iteration, or an iterator. 
# If function is None, the identity function is assumed, that is, all elements of iterable that are False are removed.

def is_even(num):
    if num % 2 == 0:
        return True
nums = [1, 2, 3, 4]
# To get the results, either iterate through filter() or cast to a list.
print(list(filter(is_even, nums)))
print(("\n"))

print(list(filter(lambda x: x%2==1, nums)))
print("\n")

# Filter function takes one iterable as an argument!
print(list(filter(lambda x: x in [1, 5, 3, 5], nums)))
print("\n")



# Lambda Expressions

# lambda_expr ::=  "lambda" [parameter_list] ":" expression
# Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. 
# The expression lambda parameters: expression yields a function object. The unnamed object behaves like a function object defined with:
""" 
def <lambda>(parameters):
    return expression
"""
# See section Function definitions for the syntax of parameter lists. Note that functions created with lambda expressions cannot contain statements or annotations.

# A lambda expression is a shorthand notation for creating small, anonymous functions in Python. 
# It is also known as a lambda function. The lambda expression is defined using the lambda keyword followed by one or more arguments, a colon, and an expression.
# The arguments are separated by commas and the expression is a single statement. 
# The lambda function returns the value of the expression.
# The basic syntax for a lambda function is as follows:
"""
lambda arguments: expression
"""

# For example, the following lambda expression takes a single argument x and squares it:
""" 
lambda x: x * x
"""
# Here is an example of using a lambda expression in the map() function to square a list of numbers:
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x * x, numbers)
print("\n")

# Lambda expressions are often used in places where a function is required as an argument, such as in the map and filter functions. 
# They are also useful when you need to create a small function for a specific purpose and don't want to define a separate named function for it. 
# They are also called throwaway functions, because they are just needed where they have been created.
# In short, a lambda expression is a small, anonymous function that is defined without a name, and it is often used in places where a function is required as an argument.
print(list(map(lambda x, y: x * y, [1, 2, 3], [2, 5, 10])))
print("\n")

print(list(filter(lambda x: x%2==1, [1, 2, 3, 4, 5, 6])))
print("\n")



# Scope
"""
In Python, the scope of a variable refers to the portion of the program where the variable can be accessed or used. It defines the visibility or accessibility of a variable.

There are two main types of scope in Python: global and local.
- A variable defined at the top level of a module, outside of any function or class, is said to have global scope. 
  It is visible and accessible throughout the entire module, including inside functions and classes.
- A variable defined inside a function or a class is said to have local scope. 
  It is only visible and accessible within that function or class.

When a variable is accessed in a program, the interpreter first checks if there is a variable with the same name in the local scope. 
If it does not find one, it will then look for the variable in the global scope. If it does not find the variable in either of these scopes, it will raise an error.

It's also worth noting that Python also has a built-in namespace, which contains all of the built-in functions, classes, and variables that are available in the Python language. 
These are available to every program without the need to import them.

Additionally, the LEGB rule is used to determine the order of precedence of the scopes in Python, Local, Enclosing, Global and Built-in.

Python also allows the use of global statement to define a variable defined inside a function or class as a global variable, 
making it available to the entire module and not just the function or class.
"""

# LEGB Rule
"""
The LEGB Rule is a rule in Python that defines the order in which the interpreter searches for a variable when it is accessed in a program. 
The acronym LEGB stands for Local, Enclosing, Global, and Built-in. The rule applies to all types of variables, including functions, classes, and module-level variables.

When the interpreter encounters a variable, it will search for it in the following order:
1) Local: The interpreter first looks for the variable in the current function or class's local namespace. 
   This includes all the variables defined within the function/class and parameters passed to the function.

2) Enclosing: If the variable is not found in the local namespace, the interpreter will look for it in the local namespaces of any enclosing functions or classes. 
   This is useful when a variable is defined in an outer function and is used in an inner function.

3) Global: If the variable is not found in the local or enclosing namespaces, the interpreter will look for it in the global namespace of the current module. 
   This includes all the variables defined at the top level of the module, outside of any function or class.

4) Built-in: If the variable is not found in any of the above namespaces, the interpreter will look for it in the built-in namespace. 
   This includes all the built-in functions, classes, and variables that are available in the Python language.

If the variable is not found in any of these namespaces, the interpreter will raise a NameError.

It's worth noting that a variable defined inside a function could be defined as global with global keyword which makes it available for the entire module and not just the function.
"""

# global statement
"""
In Python, the global statement is used to indicate that a variable is a global variable, rather than a local variable. 
It is used to indicate that a variable defined inside a function or class should be treated as a variable defined at the top level of a module, outside of any function or class.

When a variable is defined inside a function or class, it is by default considered as local variable and its scope is limited to that function or class. 
This means that the variable can only be accessed or modified within that function or class and is not available outside of it.

However, if you want to use a variable defined inside a function or class outside of it, you can use the global statement to indicate that the variable is a global variable. 
This makes the variable available for the entire module and not just the function or class.
"""
x = 5
def my_function():
    global x
    print(x)
    x = 10
    print(x)

print(x) # Prints 5
print("\n")
my_function()
print("\n")
print(x) # Prints 10

# In the above example, the variable x is defined as a global variable and it's modified by the my_function(). 
# The value of x is accessible throughout the module, not just within the function.



# EVERYTHING IN PYTHON IS AN OBJECT!
# In Python, functions are also objects and can be treated like any other type of object, such as integers, strings, or lists.
# It is possible to assign functions to variables in the same manner as numbers, utilizing the capability of functions being treated as objects in Python.

# In this example, the function my_function is assigned to the variable greeting. 
# The variable greeting now points to the same function as my_function, so calling greeting() is equivalent to calling my_function().
def my_function():
    return "Hello, World!"

greeting = my_function
print(greeting()) # prints "Hello, World!"

# You can also pass a function as an argument to another function, just like you can with any other type of object:
# In this example, the function call_function takes a function as an argument, and it is calling that function and returns the result.
def my_function():
    return "Hello, World!"

def call_function(fn):
    return fn()

print(call_function(my_function)) # prints "Hello, World!"

# This feature makes Python a powerful language, as it allows you to use functions as first-class citizens, 
# meaning that you can pass them as arguments to other functions, return them as results, and assign them to variables.