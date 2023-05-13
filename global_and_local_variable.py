"""
What's global varibale?

global variable is variable which can access on condition, function, and loop(for, while)
"""

"""
What's local varibale?

local variable is variable which can access on function and class
"""

name_user = "Jhon" #this global variable

# Example scope global and local variable
def setSchemaUser (**kwargs):
    age = kwargs["ageUser"] #local variable scope
    fromCountry = kwargs["fromCountry"] #local variable scope
    return f"My name {name_user}, my age {age} and i from {fromCountry}"

set_user_first = setSchemaUser(ageUser=25,fromCountry="Indonesia")
print(set_user_first)

# print(age) 
# print(fromCountry) 

# note: if you active print age and fromCountry result on your IDE = error, because age and fromCountry is a local variable from function setSchemaUser

# example modified value global variable
# i use type hints on argument new_name

def modifiedGlobalVariable(new_name:str):
    global name_user 
    # global from function builtin python for access global variable
    name_user = new_name
    return name_user

print(f"name user before modified: {name_user}")
modifiedGlobalVariable("Petter Thiel")
print(f"name user after modified: {name_user}")