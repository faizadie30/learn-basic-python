# i = 1
# while i < 6:
#   print(i)
#   i += 1


# with logic fiz buzz 1 to 15
n = 0
while n < 15:
    n += 1
    if n% 15 == 0:
        print("key ", n, "= FizzBuzz")
    elif n% 3 == 0:
        print("key ", n,"= Fizz")
    elif n% 5 == 0:
        print("key ", n,"= Buzz")
    else:
        print(n)


# looping triangle logic with alphabet
n=5; i=0; numAlpha = 63
while(i <= n):
  numAlpha +=1 
  #from right to left
  print(" " * (n - i) + chr(numAlpha) * i)
# from left to right
#   print(" "+chr(numAlpha) * i)
  i+=1