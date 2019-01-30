

def caesar(self, encrypt: bool, text: str, key: str):
	"""
	Replace each letter in the text by the letter
	"""
	try:
		key = int(key)

		if not encrypt:
			key = -key
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