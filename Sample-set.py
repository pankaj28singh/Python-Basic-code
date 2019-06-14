"""
set--

similar to list 

--doesnt contain duplicates
A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(type(basket))
print(basket)


print("apple" in basket)

a=set('aabcbvfasdba')
b=set('plabvfgdbavf')

print("------basic operation on sets-------")

print(a)
print(b)
print(a-b)
print(a|b)
print(a^b)