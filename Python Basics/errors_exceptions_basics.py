# ERRORS AND EXCEPTIONS HANDLING

# In Python, an exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. 
# Exceptions are raised when a program encounters an error or unexpected condition that it cannot handle, 
# and they can be caught and handled by code in the program using try-except blocks.
# Exceptions are useful for handling errors and unexpected conditions in a clean and organized way, 
# rather than using error-prone and hard-to-debug constructs such as if-else statements and return codes.

# TRY-EXCEPT-FINALLY STATEMENT
"""
try:
    # code that may raise an exception
except ExceptionType:
    # code to handle the exception
else:
    # code to run if no exception was raised
finally:
    # code to run whether an exception was raised or not
"""

def get_int():
    while True:
        try:
            num = int(input("Enter a number: "))
        except:
            print("It is not a number!")
            continue
        else:
            print("Thanks!")
            break
        finally:
            print("I always execute\n")
        print(num)
        
x = get_int()

# With a try-except-finally statement, any continue or break statements are reserved until after the try block is completed.
# This means that, even though a successful input of an integer -for example, 4- brought us to the else block, and a break statement was executed,
# the try block continued through to the finally block before breaking out of the while loop. And since print(num) was outside the try block, the
# break statement prevented it from running.