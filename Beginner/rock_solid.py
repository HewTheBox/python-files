import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

items = ["Rock","Paper","Scissors"]

man_choice = items[choice]
pc_choice = random.choice(items)

if man_choice == pc_choice:
	print("Draw!\nYou both choose " + man_choice)
elif man_choice =="Rock" and pc_choice =="Scissors":
	print("You won!\nPC choose " + pc_choice)
elif man_choice =="Scissors" and pc_choice =="Paper":
	print("You win!\nPC choose " + pc_choice)
elif man_choice =="Scissors" and pc_choice =="Rock":
	print("You loose!\nPC choose " + pc_choice)
elif man_choice =="Paper" and pc_choice =="Scissors":
	print("You loose!\nPC choose  " + pc_choice)
elif man_choice =="Paper" and pc_choice =="Rock":
	print(f"You won!\nPC choose {pc_choice}")
elif man_choice =="Rock" and pc_choice =="Paper":
	print(f"You lost!\nPC choose {pc_choice}")

