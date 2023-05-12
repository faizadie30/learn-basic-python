thisSet = {"apple","banana","black currant"}
print(thisSet)
print("type sets: ",type(thisSet))
print("count length sets",len(thisSet))

# add value on set item
thisSet.add("orange")

newItems = {"mango","avocado"}
thisSet.update(newItems)
print("add value:", thisSet)

# remove value from items
thisSet.remove("mango")
print("result form remove:",thisSet)

# access set items
for x in thisSet:
    print(x)
    
# check avail value banan or not
print("banana" in thisSet)
