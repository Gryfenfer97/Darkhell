#This code come from the FrenchMasterSword's Project cryptix : https://github.com/FrenchMasterSword/Cryptix/blob/master/
#code's file : https://github.com/FrenchMasterSword/Cryptix/blob/master/encrypt.py
#I adapted the code to be able to encode the upper case letters

def caesar(encrypt: bool, text: str, key: str):
	try:
		key = int(key)

		if not encrypt:
			key = - key
		result = ''
		for char in text:
			if char.isalpha():
				if char.isupper():
					letter = chr((ord(char) - 65 + key) % 26 + 65)
				else:
					letter = chr((ord(char) - 97 + key) % 26 + 97)
			else:
				letter = char
			result+=letter
		return result

	except ValueError:
		return "error"

	except Exception as e:
		return "error"


def vigenere(encrypt:bool, text:str, key:str):
	try:
		if not encrypt:
			encrypt = -1
		result = ''
		i=0
		for letter in text:
			if letter.isalpha():
				if letter.isupper():
					letter = chr((ord(letter) - 65 + encrypt * ord(key[i]))%26 + 65)
				else:
					letter = chr((ord(letter) - 97 + encrypt * ord(key[i]))%26 + 97)
			i+=1
			i%=len(key)
			result += letter 
		return result

	except ValueError:
		return "error"

	except Exception as e:
		return "error"


print(caesar(True,"I love you",1))
print(vigenere(False,vigenere(True,"test","ab"),"ab"))