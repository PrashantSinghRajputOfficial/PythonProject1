lists = [1,2,3,4,5]
lists[2] = 9
print(lists)
tuples = (1,2,3,4,5)
print(tuples)
set1 = {1,2,3,4,2,32}
set2 = {2,4,3,67,8}
Dictionaries = {
    "prashant": 90381 ,
      "yash" : 83989,
        "vaibhav" : 93937
}
print(Dictionaries)
Dictionaries["prashant"] = 2893938
print(Dictionaries)


fruits = ["apples", "banana", "mango"]
for fruit in fruits :
    print("- " + fruit)

for i in range(len(fruits)) :
    print(f"print {i}" + fruits[i])

lists = [1,2,3,4]
tupls = (1,2,3,4,5)
set = {1,2,3,4,5,2,4,5,3,2,1}
dictionar = {"name" : "prashant",
             "age"  : "20"
             }
print("list index 2 value is:", lists[2] )


for keyword, value in dictionar.items() :
    print(f"{keyword} : {value}")

union_set = set1.union(set2)
print(union_set)

common_topics = set1.intersection(set2)
print(common_topics)