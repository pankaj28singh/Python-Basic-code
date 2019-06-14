# learning Data structure in python list

"""
points:

1. A list in Python is a heterogeneous container for items
2. It contains duplicates
3. Lists are ordered.
4. List elements can be accessed by index
5. Lists can be nested to arbitrary depth.
6. Lists are mutable.

"""
# fullfill first condition
myList=["hello",78,89.5,[8,6]]
print("Type of myList is :" + str(type(myList)))
print(myList)

# fullfill second condition
yourList=[78,89,78,45,44,34,89]
print(yourList)

# fullfill third condition

yourList.append(100)
yourList.append(102)
yourList.append(109)
yourList.append(200)
print(yourList)

# fullfill fourth condition

print("the value of index 2 is "+str(yourList[2]))
print("the value of index 5 is "+str(yourList[5]))
print("the value of index -1 is "+str(yourList[-1]))
print("the value of index -3 is "+str(yourList[-3]))

# Lists are mutable.

# Q1. WHAT IS THE BENFIT OF IMMUTABLITY??

yourList[2]=300
yourList[-1]=500

print(yourList)

#slicing
print(yourList[2:5]) #300,45,44
print(yourList[3:]) # 45 ....
print(yourList[:-5]) # ???


# notion of containments with lists

print(89 in yourList)

if 100 in yourList:
	print("hip hip hurrah")

