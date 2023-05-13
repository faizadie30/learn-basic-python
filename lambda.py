"""
What's lambda?
lambda is function for a samll anonymous function
And a lambda function can take any number of arguments, but can only have one expression. 
"""

# example one argument
x = lambda a : a + 10
print(x(5))

# example multiple argument
x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

"""
Why use lambda?
check this bellow:
"""
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))