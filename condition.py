a = 200
b = 33
c = 500

# complex use condition if elseif else
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
# use ternary condition if elseif else
print("A") if a > b else print("=") if a == b else print("B")

# use and on condition
if a > b and c > a:
  print("Both conditions are True")
  
# use or on condition
if a > b or a > c:
  print("At least one of the conditions is True")
  
# use not on condition
if not a > b:
  print("a is NOT greater than b")
  
# nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")