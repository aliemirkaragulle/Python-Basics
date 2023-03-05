# FILE 
# In Python, a file object is used to read or write data to a file on a local or remote file system. 
# It provides a way to interact with the file system by allowing you to read, write, and manipulate files.




# Constructors

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# name
# Optional. Full filepath.

# mode
# Optional. Possible values:
# ‘r’ open for reading (default) ‘w’ open for writing, truncating the file first 
# ‘a’ open for writing, appending to the end of the file if it exists ‘b’ binary 
# mode ‘t’ text mode (default) ‘+’ open a disk file for updating (reading and writing) 
# ‘U’ universal newlines mode (for backwards compatibility; should not be used in new code)
""" 
my_file = open("test.txt", mode = "w+")
my_file.close()
"""



# Methods

# file.read([size])

# file.readlines([sizehint])

# file.write(str)

# file.writelines(iterable)

# file.seek(offset[, whence])

# file.close()



# Optimal Syntax

# I no longer need to close the file:
""" 
with open("test.txt") as my_file:
    # Something to Execute
"""



# Iterating Through a File
""" 
for line in open("test.txt"):
    print(line)
"""