listCars = [
    {"name": "jhon", "email" : "jhon@gmail.com"},
    {"name": "edward", "email" : "edward@gmail.com"}
]

# appen new data on variable listCars
listCars.append({"name": "petter thiel", "email" : "petter_thiel@gmail.com"})

# modified value index 0 
listCars[0] = {"name": "Morgan Housel", "email" : "mor_housel@gmail.com"}

# loop array list cars
for value in listCars:
    print(value)
    
# get length variable listCars
print("length value list cars:", len(listCars))

# pop listCars
newListCars = listCars.copy()
newListCars.pop(1)
print(newListCars)

# remove value object petter thiel
listCars.remove({"name": "petter thiel", "email" : "petter_thiel@gmail.com"})
print("result remove petter thiel:", listCars)