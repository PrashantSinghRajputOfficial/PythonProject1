# 1. Arithmetic Operators

num1 = int(input("Enter frist number value :"))
num2 = int(input("Enter frist number value :"))
print("you give number 1 value is :",num1)
print("you give number 2 value is :",num2)
print("Addition : ",num1," + ",num2," = ",num1+num2)
print("Subtraction : ",num1," - ",num2," = ",num1-num2)
print("Multiplication : ",num1," x ",num2," = ",num1*num2)
print("Division : ",num1," / ",num2," = ",num1/num2)
print("Floor Division(quotion) : ",num1," // ",num2," = ",num1//num2)
print("Modulus(reminder) : ",num1," % ",num2," = ",num1%num2)
print("Exponentiation(power) : ",num1," ** ",num2," = ",num1**num2)


# 2. Assignment Operators

num3 = int(input("\nEnter a number : "))
print("your given number is : ",num3)
num3 += int(input(f"give a number you want to add in priviour number : {num3} + "))
print("After addition your number : ",num3)
num3 -= int(input("give a number you want to Subtraction in priviour number : {} - ".format(num3)))
print("After Subtraction your number : ",num3)
num3 *= int(input("give a number you want to Multiplication in priviour number : {} x ".format(num3)))
print("After Multiplication your number : ",num3)
num3 /= int(input("give a number you want to Division in priviour number : {} / ".format(num3)))
print("After Division your number : ",num3)
num3 //= int(input("give a number you want to quotion in priviour number : {} // ".format(num3)))
print("After quotion your number : ",num3)
num3 %= int(input("give a number you want to reminder in priviour number : {} % ".format(num3)))
print("After reminder your number : ",num3)
num3 **= int(input("give a number you want to Exponentiation(power) in priviour number : {} ** ".format(num3)))
print("After Exponentiation(power) your number : ",num3)


# 3. Comparison Operators

num4 = float(input("\nenter your presentage : "))
print("your number is equal to 75 :",num4 == 75)
print("your number is not equal to 75 :",num4 != 75)
print("your number is greater then 75 :",num4 > 75)
print("your number is less then 75 :",num4 < 75)
print("your number is greater then equal to 75 :",num4 >= 75)
print("your number is less then equal to 75 :",num4 <= 75)


# 4. Logical Operators

print("\nregistration form :")
age = int(input("Enter your age : "))
married =input("Are you married(pleases write yes or no) : ")
if (age >= 18) and (married == "yes") :
    print("you are eligible for ragister")
else :
    print("you are not eligible for ragister")


print("\nRegistartion form :")
age = int(input("Enter your age : "))
college =input("you are in college(pleases write yes or no) : ")
if (age >= 18) or (college == "yes") :
    print("you are eligible for ragister")
else :
    print("you are not eligible for ragister")

print("\nRegistartion form :")
case1 = input("You are facing a criminal case(pleases write yes or no) : ")
if not (case1 == "yes") :
    print("you are eligible for ragister")
else :
    print("you are not eligible for ragister")


age4 = 19
college4 = "yes"
sumb = (age4 >= 18) or (college4 == "yes")
print(sumb) # it give output on bool type