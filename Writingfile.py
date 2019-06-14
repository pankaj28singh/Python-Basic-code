f= open("scores.txt","a")
while True:
	participant=input("participants name >")
	if participant=="quit":
		print("thank u everyone")
		break
	score = input("score for "+ participant+ " >")
	
	f.write(participant+","+str(score) +"\n")
f.close

"""
tasks
read a file and convert into dict
"""