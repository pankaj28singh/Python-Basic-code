"""
learning dictionary

--unordered collection of items
--a dictionary has a key: value pair
--key -> always unique
--values-> may be duplicate



More than one entry per key is not allowed ( no duplicate key is allowed)
The values in the dictionary can be of any type while the keys must be immutable like numbers, tuples or strings.
Dictionary keys are case sensitive- Same key name but with the different case are treated as different keys in Python dictionaries.


"""

ice_cream={"alice":"chocalte","rithvik":"strawberry","pankaj":"vanilla"}

print(type(ice_cream))
print(ice_cream)

#unordered collection of items
ice_cream["neha"]="chocbar"
print(ice_cream)

#a dictionary has a key: value pair

print(ice_cream["pankaj"])

#key -> always unique
ice_cream["pankaj"]="milkybar"
print(ice_cream)

#value may be duplicate

ice_cream["rohan"]="milkybar"
print(ice_cream)

#containments 
print("pankaj" in ice_cream)
print("vijay" in ice_cream)


