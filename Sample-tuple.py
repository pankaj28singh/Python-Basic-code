"""
Tuple--

a sequence of immutable Python objects.
the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
index allow


diadvanatge :
'tuple' object does not support item assignment



"""
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5,9,6,5 );
tup3 = "a", "b", "c", "d";

print(type(tup1))

print(tup1,tup2,tup3)
print(tup1[0])
print(tup1[2:])

#tup1[0]="maths" throw arrow
#print(tup1[10])

print(len(tup1))

for i in tup1:
	print(i)

tupadd=tup1+tup2
print(tupadd)