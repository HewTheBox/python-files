import math
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text,shift_number):
	cypher = ""
	for letter in plain_text:
		index = alphabet.index(letter)
		new_index = index+shift_number
		new_letter = alphabet[new_index]
		cypher+=new_letter
	print(cypher)


def decrypt(text,shift):
	decyph = ""
	for letter in text:
		index = alphabet.index(letter)
		new_index = index - shift
		new_letter = alphabet[new_index]
		decyph +=new_letter
	print(decyph)

decrypt(text,shift)
encrypt(text,shift)

