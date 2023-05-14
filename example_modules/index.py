# from math import * 
# code on top, use for import all function from file math.py

from math import addition as add, substraction as substract
# code on top, use for import function addition and substraction
# and use as for rename name function
addition = add(5,10,25,5)
print(f"result 5 + 10 + 25 + 5 = {addition}")

substraction = substract(100, 25)
print(f"result 100 - 25 = {substraction}")