# basic discussion on list

# how to create empty list?
empty_list=[]
print(type(empty_list))
print(len(empty_list))

#looping and iterating over List
names =["rithvik","pankaj","ajay","Aunubhav","Esha","Rahul","Omprakash","pooja","vikas","Umar","umesh"]
for x in names:
	print("hello "+ x)

"""

find out the list of name start with vowel ??

y ="Aankaj"
print(y[0])
print(y[0] in ["A","E","I","O","U"])
print(y[0] in "AEIOU")

"""
for x in names:
	if x[0] in "AEIOUaeiou":
		print(x + " starting with vowels")

"""
create a list of vowels names list??
"""
for x in names:
	if x[0] in "AEIOUaeiou":
		print(x + " starting with vowels")
		empty_list.append(x)
print(empty_list)

total=0
prices=[89.5,90.45,78.45,90,100]
for i in prices:
	total=total+i
print(total)

print(sum(prices))


"""
tasks1-- check even/odd lists? create lists of even and odd??
tasks2-- wap to create fibbonic series less than 200?
tasks3 -- wap to check weather number is palinodrome or not?
tasks4-- wap to print table of any number?
tasks5-- wap to check weather its  prime number or not prime ??
 