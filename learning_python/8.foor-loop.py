# Creating a Fruits list
fruits = [
    "Apple",
    "Orange",
    "Mango",
    "Banana",
    "Papaya"
]


# making a list of fruits items by using for loop :
for item in fruits:
    print(f"- {item}")


# making this list with index value :
print("\nMaking this list with indez value : ")
for index, value in enumerate(fruits, start=1): # ther enumerate is a function which give index value and start=1 means index's value starting from 1
    print(f"index{[index]} : {value}")