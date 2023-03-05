# PYTHON CONTROL FLOW

# Control Flow refers to the order in which the statements in a program are executed. 
# In Python, control flow is achieved through the use of statements such as if-else, for loops, and while loops.
# These statements allow the program to make decisions and repeat actions. This allows for the creation of more complex and dynamic programs.

# In most programming languages, including Python, there arre several control flow structures that can be used to control the order of execution of the statements in a program.
# These include:
# Conditional Statements (if-else), which allow you to execute a certain block of code only if a certain condition is True.
# Looping Statements (for, while), which allow you to repeat a block of code multiple times,
# either until a certain condition is met or for a specified number of iterations.
# Jump Statements (break, continue, pass), which allow you to change to flow of the program and jump out of loops or switch between different branches of code. 

# All of these statements work togetheer to control the flow of the program and determine what code will be executed and when.
# The use of control flow statements allows you to write code that can adapt to differrent scenarios and inputs, making it more flexible and dynamic.




# PYTHON STATEMENTS

# Conditional Statements

# If, Elif and Else 

"""
Syntax:
if condition_1:
    # code to be executed if condition_1 is True
elif condition_2:
    # code to be executed if condition_1 is False and condition_2 is True
elif condition_3:
    # code to be executed if condition_1 and condition_2 are False and condition_3 is True
else:
    # code to be executed if none of the above conditions are True

Here, condition_1, condition_2, condition_3 are the conditions that you want to check. 
The code indented under the if statement will be executed only if the condition is True, similarly for the elif and else. 
The conditions are checked in the order they are written and the first True condition will cause its corresponding code block to be executed 
and the control will be jumped out from the construct. There is no limit on the number of elif conditions that can be used. An else statement is optional.
Also worth noting, conditions can be any valid python expressions that return a boolean value, like a comparison operator, equality check, membership check etc.
"""
# Note that when the "if" condition is True, Python will not check any of the conditions in the elif or else even though they may be True.
x = 5
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")
print("\n")



# Looping Statements

# For Loops
"""
A "for" loop in Python allows you to iterate over an iterable in a definite order.
The definite order refers to the fact that the loop will iterate over the items in the sequence one by one in a specified order (usually from the first item to the last item).

The syntax for a "for" loop is:
for variable in iterable:
    # code to be executed for each iteration

Here, "variable" is a variable that takes the value of the next item in the iterable on each iteration. 
The "iterable" can be any object that can be iterated over.

The "for" loop starts by specifying the variable that will take the value of the next item in the iterable. 
Then, it uses the "in" keyword to specify the iterable. The code block that follows is intended, and it will be executed for each iteration. 
The value of the variable is updated on each iteration to the next value in the iterable. The variable can be referenced inside the loop.
"""
# Iterating over a list of numbers
numbers = [0, 1, 2, 3, 4, 5]
for num in numbers:
    print(num)
print("\n")

# While Loops
"""
A "while" loop in Python repeatedly executes a block of code while a given condition is True. The basic syntax is:

The syntax for a "while" loop is:
while condition:
    # code to be executed
The "condition" is an expression that evaluates to either True or False. 
As long as the condition is True, the code in the loop will execute. Once the condition becomes False, the loop will stop.
"""
# Print numbers 0 through 9
count = 0
while count < 10:
    print(count)
    count += 1
print("\n")

# While-Else Loops"
""" 
A "while-else" loop in Python is a loop that contains a "while" clause, followed by an "else" clause. 
The "while" clause is used to specify the condition that the loop will run on, 
and the "else" clause is executed after the loop has completed, but only if the loop completed normally.

The syntax for a "while-else" loop looks like this:
while condition:
    # code to be executed while the condition is ture
else:
    # code to be executed after the while loop completes
"""
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop Complete.")
print("\n")

count = 0
while count < 3:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print("Loop Complete.")
print("\n")



# Jump Statements

# break Statement
# The break statement breaks out of the innermost enclosing loop.
# Loop statements may have an else clause; it is executed when the loop terminates through the exhaustion of the iterable (with for) or
#  when the condition becomes false (with while), but not when the loop is terminated by a break statement.

for i in range(5):
    print(i)
    if i == 2:
        break
print("\n")

# continue Statement
# The continue statement continues with the next iteration of the loop.

for i in range(5):
    print(i)
    if i == 2:
        print(f"YES! I want {i} apples.")
        continue
    print(f"I do not want {i} apples.")
print("\n")

# pass Statement
# The pass statement does nothing.
# It can be used when a statement is required syntactically but the program requires no action.
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)
print("\n")