import random

capital_dict={
"Aghanistan": "Kabul",
"Albania": "Tirana",
"pakistan":"islamabad",
"Algerilgeria": "Algiers",
"Andorra": "Andorra la Vella",
"Angola": "Luanda",
"Antigua and Barbuda": "Saint John's",
"Argentina": "Buenos Aires",
"Armenia": "Yerevan",
"Australia": "Canberra",
"Austria": "Vienna",
"india":"delhi"
}

states_lst= capital_dict.keys()
print(states_lst)

while True:
	states=random.choice(states_lst)
	captial=capital_dict[states]
	
	captial_guess= input("what is the captial of "+ states +" ? ")
	if captial_guess == "quit":
		print("good bye")
		break
	elif captial_guess==captial:
		print("nice job ")
	else:
		print("the capital of "+states+ " is " + captial)

		
"""
tasks :

1. not case sentive
2. remove doubles quotes
"""