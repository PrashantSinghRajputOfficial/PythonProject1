# Variables & Basic Data Types

**OBJECTIVE:** Learn how to create variables, understand basic data types (integers, floats, and strings), and perform arithmetic operations in Python.

## 1. Variables in Python

### Definition:
Variables are like containers that store data. Creating a variable in Python is easy—just write the variable name, use the assignment operator (=), and assign a value.

#### Example:
```python
example = 23
print(example)
```

### Naming Conventions:
Variable names can be a combination of letters (a-z, A-Z), digits (0-9), and underscores `(_)`.  
A variable name cannot start with a digit.

#### Examples:
- `college_problem`
- `projectDescription`
- `score_2025`

### Note:
In Python, you can't use a variable without assigning a value to it first. If you try, you'll get an error.

#### Example:
```python
college_problem   # NameError: name 'college_problem' is not defined
```

### Dynamic Typing:
Python is a dynamically typed language, meaning you can assign a value to a variable without declaring its type, and Python will automatically determine the data type.

#### Example:
```python
example1 = 10        # Integer data type
example2 = "hello"   # String data type
example3 = 10.78     # Float data type
```

# 2. Basic Data Types

## A. Numbers

Python has two main types of numbers:

### 1. Integer (int):
Whole numbers that you use without decimals. 

Example: 2, 68

### 2. Float:
Decimal numbers that you use with fractional parts.

Example: 7.89, 4.8

## B. Strings

### Definition:
Strings are sequences of characters. You can write them inside single quotes `'...'` or double quotes `"..."`

### Example:
"hello everyone"

'Code with me'

#### We will continue reading about List, Tuple, Set, and Dictionary datatype further

## 3. Practice Exercise: Variable Creation & Arithmetic Operations

### Step A: Variable Creation

#### Example:

```python
Shopping_list = "Apples, Bananas, Milk, Eggs, Bread"
```

### Step B: Arithmetic Operations with Numbers (integer and float)

Python allows you to perform various arithmetic operations with numbers. The basic arithmetic operations include addition, subtraction, multiplication, division, and more.

If you perform operations by mixing integers and floats, the result automatically becomes a float

We can perform many arithmetic operations at once.

#### Basic Arithmetic Operations:

1. **Addition (`+`)**: Adds two numbers together.

Example:
```python
result = 5 + 3.7
print(result)  # Output: 8.7
```

2. **Subtraction (`-`)**: Subtracts the second number from the first.
Example:
```python
result = 10.9 - 4.6
print(result)  # Output: 6.300000000000001
```

3. **Multiplication (`*`)**: Multiplies two numbers.
Example:
```python
result = 7 * 3.98
print(result)  # Output: 27.86
```

4. **Division (`/`)**: Divides the first number by the second and returns a float.

Example:
```python
result = 20 / 4.9
print(result)  # Output: 4.081632653061225
```

5. **Floor Division (`//`)**: Divides and returns the quotient, discarding the remainder.

Example:
```python
result = 20 // 3
print(result)  # Output: 6
```

6. **Modulus (`%`)**: Returns the remainder when the first number is divided by the second.

Example:
```python
result = 20 % 3
print(result)  # Output: 2
```

7. **Exponentiation (`**`)**: Raises the first number to the power of the second number.
    
Example:

```python
result = 2.8 ** 3.9
print(result)  # Output: 55.45188606457768
```

### Example of Using Arithmetic Operations Together:

```python
num1 = 6
num2 = 98
num3 = 39
result = num1 - num2 / num3 - (num2 * num3) / num2
print(result)  # Output: -35.51282051282051
```

### **OUTCOMES:**

- Understand variable creation and dynamic typing in Python.
- Learn and apply basic data types like integers, floats, and strings.
- Perform arithmetic operations using both integers and floats.
- Gain hands-on experience with arithmetic operators and their results.