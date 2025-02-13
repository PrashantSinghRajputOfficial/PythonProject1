# we have two list

#list frist
list_1 = [1,2,3,4,5]
print("list frist : ",list_1)

#list second
list_2 = ["a","b","c","d","e"]
print("list second : ",list_2)

# Frist problem : making a list using frist and second list in alternating order
list_3 = []
for l_1,l_2 in zip(list_1,list_2):
    list_3.append(l_1)
    list_3.append(l_2)
print("making third list using 1 and second list : ",list_3)

# Second problem : make a dynamic list using first and second list, there list charactor in key and integer is value
list_4 = []
for l_3,l_4 in zip(list_1,list_2):
    list_4.append({l_4 : [l_3]})
print("dynamic list making using frist and second list : ",list_4)

# Third problem : make a dynamic list using third list, there list charactor in key and integer is value
list_4_2 = []
for i in range(0, len(list_3), 2):
    value = list_3[i]
    key = list_3[i+1]
    list_4_2.append({key : [value]})
print("dynamic list making using list third : ",list_4_2)

# Fourth porblem : makin again third list using dynamic list
new_list_3 = []
for item in list_4:
    for keyword, value in item.items() :
        for main in value:
            new_list_3.append(main)
            new_list_3.append(keyword)
print("remakin list 3 using dynamic list : ",new_list_3)

# fifth porblem : makin again second list using dynamic list
new_list_2 = []
for item1 in list_4:
    for keyword1, value1 in item1.items() :
        new_list_2.append(keyword1)
print("remakin list 2 using dynamic list : ",new_list_2)

# sixth porblem : makin again frist list using dynamic list

new_list_1 = []
for item2 in list_4:
    for keyword2, value2 in item2.items():
        for main2 in value2:
            new_list_1.append(main2)
print("remakin list 1 using dynamic list : ",new_list_1)

# Creating a Fruits list
fruits = [
    "Apple",
    "Orange",
    "Mango",
    "Banana",
    "Papaya"
]
print("\nMaking a fruits list : ",fruits)


# creating a number list
fruits2 = [
    1,
    2,
    3,
    4,
    5
]
print("Making a number list : ",fruits2)


# Porblem Solving Mindset
# Making dynamic list using my logic 
fruits3 = []

for index,value4 in enumerate(fruits,start=1):
    for index2,value5 in enumerate(fruits2,start=1):
        if (index == index2):
            fruits3.append([value4,[value5]])
print("Making a dynamic list using my another logic : ",fruits3)
