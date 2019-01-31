from datetime import datetime

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
	message += " {0} %".format(int((datetime.now().day / 365)*100))
	return message