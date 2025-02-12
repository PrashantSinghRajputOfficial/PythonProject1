# Python Syntax Basics & Comments
**OBJECTIVE:** To understand Python syntax, the importance of indentation, and how to use single-line and multi-line comments effectively in code.

## Python Statements & Newlines:

In Python, each statement is generally written on a new line:

```python
print("Hello, World!")
print("Python is fun!")
print()  # blank line for better readability
```

If you want to write multiple statements on the same line, you can separate them using a semicolon (`;`):

```python
print("hello, world!"); print("python is fun!")
print()
```

## Importance of Indentation:

It is essential to give each code block consistent indentation (generally using 4 spaces or 1 tab):

```python
if 5 > 2:
    print("Five is greater than two")  # output: Five is greater than two
```

```python
# Error due to incorrect indentation:
if 5 > 2:
print("Five is greater than two")  # Indentation Error
```

## Line Continuation:

If you need to write a long expression across multiple lines, you can use a backslash (`\`) or enclose the expression in parentheses, brackets, or curly braces:

### Using backslash:

```python
total = 1 + 2 + 3 + \
        4 + 5 + 6
print(total)
```

### Using parentheses:

```python
total = (1 + 2 + 3 +
         4 + 5 + 6)
print(total)
print()
```
### using brackets:

```python
total = [1 + 2 + 3 +
         4 + 5 + 6]
print(total)
print()
```

### using curly braces

```python
total = {1 + 2 + 3 +
         4 + 5 + 6}
print(total)
print()
```
## Comments:
### Single-line Comments:

For single-line comments, the `#` symbol is used:

#### Example of a multi-line comment:
```python
# Single-line comment:
print("single line statement")  # This is also a comment that explains the print statement.
```

### Multi-line Comments:

In Python, multi-line comments are written using triple quotes (''' ... ''' or """ ... """).

#### Example of a multi-line comment:

```python
'''
In this section, we are writing some more print statements
that demonstrate Python's syntax and indentation.
'''
```
**OUTCOMES:**

- Understand Python syntax and how to write statements on separate lines or the same line using semicolons.
- Learn the importance of consistent indentation in defining code blocks and avoiding errors.
- Gain knowledge of line continuation techniques using backslashes, parentheses, brackets, or curly braces.
- Single-line comments and multi-line comments for better code documentation and readability.