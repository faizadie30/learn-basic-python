def calculate(a,b,method="another"):
    if(method == "addition"):
        return a + b
    elif(method == "substraction"):
        return a - b
    elif(method == "multiplication"):
        return a * b
    elif(method == "division"):
        return round(a / b)
    elif(method == "modulus"):
        return a % b
    elif(method == "exponentiation"):
        return a ** b
    else:
        return a // b
    

#supprot with parameter name & value only & setup default value on function
addition = calculate(b=10,method="addition",a=20)
print("addition: ",addition)

substraction = calculate(20,5,"substraction")
print("substraction: ",substraction)

multiplication = calculate(20,5,"multiplication")
print("multiplication: ",multiplication)

division = calculate(20,5,"division")
print("division: ",division)

modulus = calculate(20,5,"modulus")
print("modulus: ",modulus)

exponentiation = calculate(20,5,"exponentiation")
print("exponentiation: ",exponentiation)

floor_division = calculate(20,5)
print("floor_division: ",floor_division)