"""
state captial Quizzers

"""
import random
import logging

logging.info("dictionary is created")


countries={
"Afghanistan": "Kabul",
"Albania": "Tirana",
"Algeria": "Algiers",
"Andorra": "Andorra la Vella",
"Angola": "Luanda",
"Antigua and Barbuda": "Saint John's",
"Argentina": "Buenos Aires",
"Armenia": "Yerevan",
"Australia": "Canberra",
"Austria":" Vienna",
"Azerbaijan": "Baku",
"The Bahamas": "Nassau",
"Bahrain": "Manama",
"Bangladesh": "Dhaka",
"Barbados": "Bridgetown",
"Belarus": "Minsk",
"Belgium": "Brussels",
"Belize": "Belmopan",
"Benin": "Porto-Novo",
"Bhutan": "Thimphu",
"Bolivia": "La Paz (administrative); Sucre (judicial)",
"Bosnia and Herzegovina": "Sarajevo",
"Botswana": "Gaborone",
"Brazil": "Brasilia",
"Brunei": "Bandar Seri Begawan",
"Bulgaria": "Sofia",
"Burkina Faso": "Ouagadougou",
"Burundi": "Gitega (changed from Bujumbura in December 2018)",
"Cambodia": "Phnom Penh",
"Cameroon": "Yaounde",
"Canada": "Ottawa",
"Cape Verde": "Praia",
"Central African Republic": "Bangui",
"Chad": "N'Djamena",
"Chile": "Santiago",
"China": "Beijing",
"Colombia": "Bogota",
"Comoros": "Moroni",
"Congo, Republic of the": "Brazzaville",
"Congo, Democratic Republic of the": "Kinshasa",
"Costa Rica": "San Jose",
"Cote d'Ivoire: Yamoussoukro (official)": "Abidjan (de facto)",
"Croatia": "Zagreb",
"Cuba": "Havana",
"Cyprus": "Nicosia",
"Czech Republic": "Prague",
"Denmark": "Copenhagen",

"Djibouti": "Djibouti",
"Dominica": "Roseau",
"Dominican Republic": "Santo Domingo",
"East Timor (Timor-Leste)": "Dili",
"Ecuador": "Quito",
"Egypt": "Cairo",
"El Salvador": "San Salvador",
"Equatorial Guinea": "Malabo",
"Eritrea": "Asmara",
"Estonia": "Tallinn",
"Ethiopia": "Addis Ababa",
"Fiji": "Suva",
"Finland": "Helsinki",
"France": "Paris",
"Gabon": "Libreville",
"The Gambia": "Banjul",
"Georgia": "Tbilisi",
"Germany": "Berlin",
"Ghana": "Accra",
"Greece": "Athens",
"Grenada": "Saint George's",
"Guatemala": "Guatemala City",
"Guinea": "Conakry",
"Guinea-Bissau": "Bissau",
"Guyana": "Georgetown",
"Haiti": "Port-au-Prince",
"Honduras": "Tegucigalpa",
"Hungary": "Budapest",
"Iceland": "Reykjavik",
"India": "New Delhi",
"Indonesia": "Jakarta",
"Iran": "Tehran",
"Iraq": "Baghdad",
"Ireland": "Dublin",
"Israel": "Jerusalem*",
"Italy": "Rome",
"Jamaica": "Kingston",
"Japan": "Tokyo",
"Jordan": "Amman",
"Kazakhstan": "Astana",
"Kenya": "Nairobi",
}
logging.info("creatings lists of states")
states=list(countries.keys())
logging.info("NOW WE ARE ITERATING")
while True:
	
	state=random.choice(states)
	capital=countries[state]
	
	captial_guess= input("what is the captial of "+ state +" ? ")
	if captial_guess=="quit":
		print("good bye")
		break
	if captial_guess==capital:
		print("good answer")
	else:
		print("wrong answer")
	
logging.info("job sucessfully run")	

	

