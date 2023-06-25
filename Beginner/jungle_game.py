print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

choice1 = input("Do you want to go left or right? ").lower()
if choice1 =="right":
	print("Game over")
elif choice1 == "left".lower():
	choice2 = input("do you want to swim or wait for a boat? ").lower()
	if choice2 =="swim":
		print("Game over")
	else:
		choice3 = input("which door do you want to enter? ").lower()
		if choice3 == "blue":
			print("Game over")
		elif choice3 =="red":
			print("Game over")
		else:
			print("You Win!! \nTreasure Discovered")
