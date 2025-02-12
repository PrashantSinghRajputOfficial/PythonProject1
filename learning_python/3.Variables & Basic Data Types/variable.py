# Variables & Basic Data Types

example = 23
print(example)

# auto define datatype

example1 = 10 # Integer data type
example2 = "hello" # String data type
example3 = 10.78 # Float data type
example4 = True # bool data type

print(type(example1), type(example2), type(example3), type(example4)) # Output: <class 'int'> <class 'str'> <class 'float'> <class 'bool'>

# Arithmetic Operations with Numbers (integer and float)

result = 5 + 3.7
print(result)  # Output: 8.7

result = 10.9 - 4.6
print(result)  # Output: 6.300000000000001

result = 7 * 3.98
print(result)  # Output: 27.86

result = 20 / 4.9
print(result)  # Output: 4.081632653061225

result = 20 // 3
print(result)  # Output: 6

# We can perform many arithmetic operations at once.
num1 = 6
num2 = 98
num3 = 39
result = num1 - num2 / num3 - (num2 * num3) / num2
print(result)  # Output: -35.51282051282051
