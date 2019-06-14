"""
while loopin python
"""

name = ["pankaj","trushan","rita"]

for i in name:
	print("hello "+ i)
	
for i in [0,1,2,3,4]:
	print("hello "+str(i))

counter=0
while counter<5:
	print("hello "+str(counter))
	counter=counter+1

print("------infintyloop-----")	
r=0
while True:
	print("Hello "+str(r))
	r=r+1
	if r>=5:
		break