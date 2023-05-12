myTuple = ("apple","banana","cherry")
print(myTuple)
print("count tuple value length:", len(myTuple))
print("check type tuple:", type(myTuple))
print("access value banana from tupple:",myTuple[1])

#update tuple
listFruits = list(myTuple)
listFruits[1] = "kiwi"
x = tuple(listFruits)

print(x)

# unpack tuple
(a,b,c) = myTuple
print(a)
print(b)
print(c)

# loop tuple
for x in listFruits:
    print(x)

# join tuple
newValFruits = ("mango","black currant")
fruits = myTuple + newValFruits
print(fruits)