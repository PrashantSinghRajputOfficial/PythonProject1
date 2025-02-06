# Python Statements & Newlines:
# In Python, each statement is generally written on a new line:
print("Hello, World!")
print("Python is fun!")
print() #blank line for better readability

# If you want to write multiple statements on the same line, you can separate them using a semicolon (`;`):
print("hello, world!"); print("python is fun!")
print()


# Importance of Indentation:
# It is essential to give each code block consistent indentation (generally using 4 spaces or 1 tab):
if 5 > 2:
    print("Five is greater than two") # output: Five is greater than two
    print()

'''
if 5 > 2:
print("Five is greater than two") # Indentation (Error)
'''

# Line Continuation:
# If you need to write a long expression across multiple lines, you can use a backslash (`\`) or enclose the expression in parentheses, brackets, or curly braces:
# using backslash:
total = 1 + 2 + 3 + \
        4 + 5 + 6
print(total)

# using parentheses:
total = (1 + 2 + 3 +
         4 + 5 + 6)
print(total)
print()

# For single-line comments, the `#` symbol is used:
# Single-line comment:
print("single line statement") # This is also a comment that explains the print statement.


# In Python, multi-line comments are written using triple quotes (''' ... ''' or """ ... """).
#Example of a multi-line comment:
'''
In this section, we are writing some more print statements
that demonstrate Python's syntax and indentation.
'''
