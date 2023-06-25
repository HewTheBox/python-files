import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def play(level,number):
	"""Takes a level of difficulty and a random number to make the game run"""
	#set difficulty
	if level == "easy":
		count = EASY_LEVEL_TURNS
	elif level =="hard":
		count = HARD_LEVEL_TURNS

	#take guess and repeat as long as there is still life
	while count > 0:
		
		print(f"You have {count} attempts to guess the number.")
		guess = int(input("Make a guess: "))

		if guess > number or guess < number and count ==1:
			if guess > number:
				print("Too high")
			else:
				print("Too low")
		elif guess > number:
			print("Too high\nGuess Again")
		
		elif guess < number:
			print("Too low\nGuess Again")
	
		elif guess == number:
			print(f"You've got it! The answer was {number}")
			count = 0
		count-=1

		if (guess > number or guess < number) and count ==0:
			print("You've run out of guesses, you lose.")
			print(f"The number is {number}")


number = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
play(level,number)
