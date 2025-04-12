# i am making a code using while loop for cheking eligibleity and sthoring phone number 
while True:
    while True:  
        try:
            age = int(input("Enter your age in number for cheking yor are eligible for this verification : "))
            break  
        except ValueError:
            print("Invalid input! Please enter your age correctly in numbers.")
    if age>=18 and age<120:
     print("You are eligible : ")
     break
    elif age<18 and age>0:
     print("you are not eligible 'sorry' ")
     exit()
    else:
     print("This age is not possibe please write correct age")
list_of_number_or_name = []
fix = True
while True :
    while True:
            qna1 = input("\nyou want to save any person phone number : ")
            if qna1.lower() == "yes":
                break
            elif qna1.lower() == "no":
                 print("Ok sir, stored phone number list is completed")
                 fix = False
                 break
            else:
                print("Please enter yes or no only")
    if fix == False:
        break
    else:
        print()
    while fix:
        name = input("person name : ")  
        try:
            num = int(input(f"Enter {name}'s Number : "))

            break  
        except ValueError:
            print("Invalid input! Please enter phone number correctly in numbers.")

        print(f"{name}'s number are saved")
            
    list_of_number_or_name.append(f"{name} : {num}")
        
if not list_of_number_or_name:
    print("you dont give any number")
else:
    for value in list_of_number_or_name:
        print("your saved number are : ")
        print(f"- {value}")
    