import random
word_list = ["ardvark","baboon","beekeeper","camel"]
word = random.choice(word_list)
print(f"Pssst, the solution word is {word}")


size = len(word)
blanks = []
i =0
final=[]
while size>0:
	blanks.append("_")
	final+=word[i]
	size-=1
	i+=1
lives = 6
end_of_game = False
while not end_of_game and lives!=0:
	char = input("enter a character ").lower()
	if char in blanks:
		print(f"You have already entered '{char}'")
	elif char not in word:
		print(f"You guessed wrong, you lose a life. You entered '{char}'")
	for i in range(0,len(word)):
		if word[i]==char:
			isIn = word[i]
			blanks[i]=word[i]

	print(f"{word}\n{blanks}")
	if '_' not in blanks:
		end_of_game = True
		print("You Win")
	elif char not in word:
		lives-=1
	if lives ==0:
		print("You loose")

	


print("Game over!")





