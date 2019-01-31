#!Python-3.6.8/python

from bot import Darkhell
import json
import os

config_file = "bot/config.json"

with open(config_file,"r") as file:
	config = json.loads(file.read())


def run_bot():
	bot = Darkhell(config)
	bot.run(config['informations']['token'])

if __name__ == '__main__':
	run_bot()