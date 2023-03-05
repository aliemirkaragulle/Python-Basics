# STRINGS = IMMUTABLE SEQUENCE (ORDERED SET) OF CHARACTERS
text = "Hello, this is a string for a trial, and an experiment."
l1 = ["Hello", "I", "was", "here!"]



# Iterable Unpacking
string = "Joe"
char0, char1, char2 = string
print(char0)
print(char1)
print(char2)
print("\n")


# Sequence Indexing and Slicing

# Indexing
first_char = text[0]
print(first_char)

# Slicing
first_three_chars = text[0:3]
print(first_three_chars)
print("\n")


# Sequence Concatenation and Multiple Concatenation (Not an In-Place Modification Since Strings are Immutable)

# Concatenation
name = "Pam"
new_name = "S" + name[1:]
print(new_name)

name = "Pam"
name = name + " Joe"
print(name)

# Concatenation Assignment
name = "Pam"
name += " Joe"
print(name)

# Multiple Concatenation
name = "Pam"
name = name * 5
print(name)

# Multiple Concatenation Assignment
name = "Pam"
name *= 5
print(name)
print("\n")



# Sequence Methods

# str.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.

# str.count(sub[, start[, end]])
number_of_a = text.count("a")
print(number_of_a)



# String Methods 

# str.join(iterable)
joined_str = " ".join(l1)
print(joined_str)

# str.split(sep=None, maxspliit=-1)
splitted_str = text.split()
print(splitted_str)

# str.splitlines(keepends=False)
line = "Hello\nIt\nis\nme\n"
splitted_lines = line.splitlines()
print(splitted_lines)

# str.strip([chars])
stripped_str = text.strip("Hello, ")
print(stripped_str)

# str.find(sub[, start[, end]])
found = text.find("a")
print(text[found])
print(found)

# str.replace(old, new[, count])
replace_a_with_X = text.replace("a", "X")
print(replace_a_with_X)

# str.isalpha()
is_alpha = text.isalpha()
print(is_alpha)

# str.isdigit()
is_digit = text.isdigit()
print(is_digit)

# str.format(*args, **kwargs)
formatted_str = "2 + 3 equals to {}".format(2+3)
print(formatted_str)
print("\n")



# String Formatting

# 1) Print Formatting
# This method involves the use of the "%" operator to place placeholders in the string,
# which are then replace with values when the string is printed.
age = 199
print("I am %s years old." %"100")
print("I am %s years old and my friend is %s years old." %("100", "99"))
print("The total age of me and my friend is %i" %age)

# Format Conversion Methods
# Two methods %s and %r converts any Python Object to a string using two separate methods: str() and repr().
# Note that %r and repr() deliver the string representation of the object, including quotation marks and escape characters.
print("Hi %s" %"\tJosh")
print("Hi %r" %"\tJosh")

# The %s operrator converts whatever it sees into a string, including int and float.
# The %d operator converts numbers to integers first, without rounding.
print("%s" %3.75)
print("%d" %3.75)

# Padding and Precision of Floating Point Numbers
# Floating point numbers use the format %width.precisionf.
# Here, width is the minimum numhber of characters the string should contain;
# these may be paddeed with whitespace if the entire number does not have this many digits.
# Next to this, .precisionf stands for how many numbers to show past the decimal point.
print("%5.2f" %0.5)

# Multiple Formatting
# Nothing prohibits using more than one converrsion tool in the same print statement.
print("1 = %s, 2 = %5.2f, 3 = %r" % ("Hi", 3.1415, "Bye"))

# 2) String Formatting
# This method involves the use of the ".format()" method, which is called on a string
# and is passed values to be placed in the placeholders within the string.
# "String here {} then also {}".format("something1", "something2")
print('This is a string with an {}'.format('insert'))

# Advantages over the Print Formatting:
# Inseted objects can be called by index position
print('The {2} {1} {0}'.format('fox','brown','quick'))
# Inserted objects can be assigned keywords
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
# Inserted objects can be re-used, avoiding duplication
print('A %s saved is a %s earned.' %('penny','penny'))
# vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))

# Alignment, Padding, and Precision with .format()
# Padding = {value:width}
# Padding & Precision = {value:width.precisionf}
# Here, value refers to an index, or a keyword.
print('This is my ten-character, two-decimal number:%10.2f' %13.579)
# vs.
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))
# By default, `.format()` aligns text to the left, numbers to the right. You can pass an optional `<`,`^`, or `>` to set a left, center or right alignment:
print("{0:8}|{1:9}".format("Fruit", "Quantity"))
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
# You can precede the aligment operator with a padding character
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

# 3) Formatted String Literals (f-strings)
# F-Strings are a way to embed expressions inside string literals in Python, using
# {} placeholders and the "f" prefix.
var = "f-string"
print(f"This is an {var}.")

# Advantages over the String Formatting
# F-Strings can bring outside variables immediately into the string rather than pass them as arguments through .format(var)
name = "Fred"
print(f"He said his name is {name}")
# Pass !r to get the string representation
print(f"He said his name is {name!r}")

# Float Formatting
# result = {value:{width}.{precision}}
# Where with the .format() method you might see {value:10.4f}, with f-strings this can become {value:{10}.{6}}
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
# Note that with f-strings, precision refers to the total number of digits, not just those following the decimal. 
# This fits more closely with scientific notation and statistical analysis. Unfortunately, f-strings do not pad to the right of the decimal, even if precision allows it.
num = 23.45
print("My 10 character, four decimal number is:{0:10.2f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{4}}")
# If this becomes important, you can always use .format() method syntax inside an f-string:
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")