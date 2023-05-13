listFruits = ["apple","banana","mango","cherry","black currant"]
for x in listFruits:
    print(x)
    
# logic fizz buzz for loop 
for i in range(15):
    i +=1
    if i % 15 == 0:
        print("key ",i,"= FizzBuzz")
    elif i % 3 == 0:
        print("key ",i,"= Fizz")
    elif i % 5 == 0:
        print("key ",i,"= Buzz")
    else:
        print(i)
        
numAlpha = 64
n = 6
iValue = 0
for inVal in range(iValue,n):
    #from right to left
    # print(" " * (n - inVal) + chr(numAlpha) * i)
    # from left to right
    print(" "+chr(numAlpha) * inVal)
    i+=1
    numAlpha +=1