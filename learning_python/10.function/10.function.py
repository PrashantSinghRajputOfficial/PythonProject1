# I am giving two parameters (a, b) in the function 'sum' 
# and inside the function, I am printing a statement
def sum(a,b):
    print("Additon of your's giving number : ",a+b)  
print("Enter 2 number :")
while True:
    try:
        num1 = int(input("frist number value: ")) 
        num2 = int(input("second number value: "))
        break
    except ValueError:
        print("Enter integer value (For Ex- 1,2...)")
sum(num1,num2)

def fullfeel(person):
    print(f"hello {person} welcome to over problem solving mindset")
while True:
    try:
        name = (input("Enter your name: "))
        break
    except ValueError:
        print("Enter string value (For Ex- rahul,yuvraj....)")
fullfeel(name)