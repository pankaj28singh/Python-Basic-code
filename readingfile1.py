f=open("country.txt","r")
countries=[]
for line in f:
	line=line.strip()
	countries.append(line)

f.close()
print(countries)
print(len(countries))

"""
tasks 
Reading from file
1. create list of countrry start with vowels.
2. create list of country strat with consonant
"""