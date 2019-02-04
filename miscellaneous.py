from datetime import datetime
import random
import json

joke_file = "bot/jokes.json"
with open(joke_file,"r") as file:
	jokes_information = json.loads(file.read())



def year_progress():
	message = ""
	black_square = ":black_medium_square:"
	white_square = ":white_medium_square:"
	days = (datetime.now() - datetime(datetime.now().year,1,1)).days
	days = int(days / 5) #on a divisé le nombre de jour de l'année par 5
	for i in range(73):
		if i < days:
			message += black_square
		else:
			message+=white_square
	message += " {0} %".format(int(((datetime.now() - datetime(datetime.now().year,1,1)).days / 365)*100))
	return message

def joke(categorie):
	if categorie == "all":
		categorie = jokes_information["categories"][random.randrange(0,len(jokes_information["categories"]))] #choix de la catégorie
	return "```{0}```".format(jokes_information[categorie][random.randrange(0,len(jokes_information[categorie]))])