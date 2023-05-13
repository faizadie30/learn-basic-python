"""
The special syntax **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).

1. A keyword argument is where you provide a name to the variable as you pass it into the function.
2. One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
"""

def math(*tupleNumber, **kwargs):
    output = 0;
    if kwargs["option"] == "addition":
        for val_number in tupleNumber:
            output += val_number
            
    elif kwargs["option"] == "multiplication":
        output = 1
        for val_number in tupleNumber:
            output *= val_number
    
    else:
        print("no execute arithmetic")
    
    return output

result_addition = math(1,2,3,4,5,6,7,8,9,19, option = "addition")
print(result_addition)

result_multiplication = math(4,10,20, option = "multiplication")
print(result_multiplication)