# Write a Python program that takes an integer input from the user and checks whether the number is positive, negative, or zero.

try :
    value = int(input("enter a number"))
except ValueError:
    print ("Enter a valid number")
    exit()

if (value == 0):
    print("your value is zero",value)
elif(value < 0):
    print("your value is nagative",value)
else : (value > 0)
print("your value is positive",value)

# Ek program likho jo user se ek number input le aur check kare ki number even hai ya odd.

try :
    value2 = int(input("enter a number"))
except ValueError:
    print ("Enter a valid number")
    exit()

if (value2 % 2 == 0):
    print("your value is even",value2)

else : (value2 % 2 != 0)
print("your value is odd",value2)

# Write a Python program that takes three numbers as input from the user and determines the largest among them.

try :
    value01 = int(input("Enter frist value : "))
    value02 = int(input("Enter second value : "))
    value03 = int(input("Enter third value : "))
except ValueError:
    print("Enter a valid input")
    exit()
if(value01 > value02 and value01 > value03):
    print(value01," is greater")
elif(value02 > value01 and value02 > value03):
    print(value02," is greater")
elif(value03 > value01 and value03 > value02):
    print(value03," is greater")
elif(value01 == value02 and value01 == value03):
    print("all number is equal : ",value01)
elif(value01 == value02 and value01 > value03):
    print(value01," is greater. There are frist and second value are same")
elif(value01 == value03 and value01 > value02 ):
    print(value01," is greater There are frist and third value are same")
elif(value02 == value03 and value02 > value01):
    print(value02, "is greater. Second and third values are same")
else:
    print("sorry i dont find this conditiom")