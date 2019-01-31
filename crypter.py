#This code come from the FrenchMasterSword's Project cryptix : https://github.com/FrenchMasterSword/Cryptix/blob/master/
#code's file : https://github.com/FrenchMasterSword/Cryptix/blob/master/encrypt.py

def caesar(encrypt: bool, text: str, key: str):
	"""
    Replace each letter in the text by the letter
    """

	try:
		key = int(key)


		if not encrypt:
			key = - key
		result = ''
		for char in text:
			if char.isalpha():
				letter = char.upper()
				letter = chr((ord(letter) - 65 + key) % 26 + 65)
			if char.islower():
				letter = letter.lower()
			else:
				letter = char
			result += letter
		return result

	except ValueError:
		return "error"

	except Exception as e:
		return "error"