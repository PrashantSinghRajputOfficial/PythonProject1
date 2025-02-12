# Python Statements & Newlines:
print("Hello, World!")
print("Python is fun!")
print() #blank line for better readability

print("hello, world!"); print("python is fun!")
print()


# Importance of Indentation:
if 5 > 2:
    print("Five is greater than two") # output: Five is greater than two
    print()

'''
if 5 > 2:
print("Five is greater than two") # Indentation (Error)
'''

# Line Continuation:
# using backslash:
total = 1 + 2 + 3 + \
        4 + 5 + 6
print(total)

# using parentheses:
total = (1 + 2 + 3 +
         4 + 5 + 6)
print(total)
print()

# using brackets:
total = [1 + 2 + 3 +
         4 + 5 + 6]
print(total)
print()

# using curly braces
total = {1 + 2 + 3 +
         4 + 5 + 6}
print(total)
print()

# Single-line comment:
print("single line statement") # This is also a comment that explains the print statement.


#Example of a multi-line comment:
'''
In this section, we are writing some more print statements
that demonstrate Python's syntax and indentation.
'''

"""
In this section, we are writing some more print statements
that demonstrate Python's syntax and indentation.
"""
