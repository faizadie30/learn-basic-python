"""
What is Python *args?
The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list. 

1. The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
2. What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
3. For example, we want to make a multiply function that takes any number of arguments and is able to multiply them all together. It can be done using *args.
Using the *, the variable that we associate with the * becomes iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.
"""


def calculate(*dataNumber):
    addition_cal = 0
    for val_number in dataNumber:
        addition_cal += val_number
    
    return addition_cal

# args for calculate addition
res_cal_addition = calculate(1,2,3,4,5,6,7,8)
print(f"result calculate addition from multiple data: {res_cal_addition}")

res_cal_addition = calculate(20,10,5)
print(f"result calculate addition from multiple data: {res_cal_addition}")