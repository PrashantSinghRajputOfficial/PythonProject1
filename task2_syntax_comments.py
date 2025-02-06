# Ye script "Hello, World!" aur basic Python syntax ko demonstrate karti hai.

# Single-line comment: Niche wale line mein "Hello, World!" print hoga.
print("Hello, World!")  # Ye bhi ek comment hai jo print statement ko explain karta hai.

# Multi-line comment ka example:
'''
Is section mein hum kuch aur print statements likh rahe hain
jo Python ke syntax aur indentation ko dikhate hain.
'''

# Ek aur print statement
print("Python Syntax Basics")
print("Indentation is crucial in Python")

num1 = 10
num2 = 4
# Floor Division (integer result)
floor_div_result = num1 // num2
print("Floor Division:", floor_div_result)  # Expected Output: 3
mod_result = num1 % num2
print("Modulus:", mod_result)  # Expected Output: 1
f1 = 5.5
result = num1 + f1
print("Mixed Addition:", result)  # Expected Output: 15.5 (if num1 is 10 and f1 is 5.5)

# Task 3: Variables & Basic Data Types

# Step 1: Create a variable for mini project description
college_problem = "India ke colleges zyadatar profit oriented hote hain, jahan learning pe focus kam hota hai. Hamara project is problem ko solve karne ke liye hai."
print("Mini Project Description:")
print(college_problem)
print()  # Blank line for better readability

# Step 2: Perform arithmetic operations with integers
num1 = 10
num2 = 3

print("Arithmetic Operations with Integers:")
print("Addition:", num1 + num2)          # 10 + 3 = 13
print("Subtraction:", num1 - num2)         # 10 - 3 = 7
print("Multiplication:", num1 * num2)      # 10 * 3 = 30
print("Division:", num1 / num2)            # 10 / 3 ≈ 3.3333
print("Floor Division:", num1 // num2)     # 10 // 3 = 3
print("Modulus:", num1 % num2)             # 10 % 3 = 1
print()  # Blank line

# Step 3: Perform arithmetic operations with floats
f1 = 5.5
f2 = 2.0

print("Arithmetic Operations with Floats:")
print("Addition:", f1 + f2)               # 5.5 + 2.0 = 7.5
print("Multiplication:", f1 * f2)         # 5.5 * 2.0 = 11.0

# Step 4: Combine integer and float arithmetic
mixed_result = num1 + f1
print("Mixed Addition (Integer + Float):", mixed_result)  # 10 + 5.5 = 15.5