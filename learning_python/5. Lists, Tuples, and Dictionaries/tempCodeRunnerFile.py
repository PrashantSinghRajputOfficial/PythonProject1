lists = [1,2,3,4,5]
print("list is ",lists)
lists[2] = 9
print("after changing index[2] value : ",lists)

tuples = (1,2,3,4,5)
print("value of index[2] is : ",tuples[2])

set1 = {1,2,3,4,2,32}
print("Set1 is : ",set1)
set2 = {2,3,4,6,7}
print("Set2 is : ",set2)
set3 = set1.intersection(set2)
print("intersection of set1 and set2 is : ",set3)
set3 = set1.union(set2)
print("union of set1 and set2 is : ",set3)

Dictionaries = {
    "prashant": 90381 ,
    "yash"    : 83989 ,
    "vaibhav" : 93937
}
print("Dictionarie is : ",Dictionaries)
Dictionaries["prashant"] = 2893938
print("After changing the prashant's value, the Dictionarie : ",Dictionaries)
