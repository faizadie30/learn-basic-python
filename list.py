thisList = ["apple","banana","cherry"]
print("print value list: ", thisList ) #print value
print("print type: ", type(thisList)) #check type data
print("print length", len(thisList)) #for count length
print("get list with value: ", thisList[1])
print("get value on list with last value: ", thisList[-1])

#change value on list
thisList[1] = "mango"
print(thisList)


# add value on list
thisList.append('avocado')
print(thisList)

# add value on first list
thisList.insert(0,"banana")
print(thisList)

# add extend on list
extendTuple = ("kiwi","black currant") # support use () or []
thisList.extend(extendTuple)
print(thisList) 

# sort list a - z or 1 - 10
thisList.sort()
print(thisList)

# sort reverse
thisList.reverse()
print(thisList)

# Copy value variable
listFruits = thisList.copy()
print(listFruits);

# remove value banana
listFruits.remove('banana')
print(listFruits)

# looping list fruits
for i in range(len(listFruits)):
    print(i, listFruits[i])

"""
note:
list not same with array
"""