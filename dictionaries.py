# example dict version 1
thisBrand = {
    "brandName":"Erigo",
    "model":"Modern Fashion",
    "category":{"tshirt","chinos","hoodie"}
}

# example dict version 2
thisCarBrand = dict(brandName="Toyota",countryFrom="Japan")
print(thisCarBrand)

print(thisBrand);
print("get value category:",thisBrand["category"])
print("length value on variable brand :",len(thisBrand))
print("type variable brand :",type(thisBrand))

# access countryFrom from variable thisCarBrand
countryFrom = thisCarBrand["countryFrom"] #support use .get("your key dictionaries  ")
print("Toyota from country?",countryFrom) 

# access all key only and value only
allKey = thisCarBrand.keys()
print("origin keys",allKey)
allValue = thisCarBrand.values()
print("origin value:",allValue)

thisCarBrand["category"] = {"manual","automatic","electric"}
allKey = thisCarBrand.keys()
print("add keys:",allKey)
allValue = thisCarBrand.values()
print("add value:",allValue)

# change value variable car
thisCarBrand.update({"countryFrom":"USA","brandName":"Tesla"}) #with methode update
print("result change all value:",thisCarBrand)

thisCarBrand["brandName"] = "Ford" #change 1 value only from key
print(thisCarBrand)

# loop dictionaries
for value in thisCarBrand.values():
    print("loop val:",value)
    
# nested dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)