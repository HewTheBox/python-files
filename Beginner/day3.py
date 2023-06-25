height = 121

if height > 120:
	age = int(input("Enter your age "))
	if age <= 12:
		print("You are paying $5")
	elif age <=18:
		print("You are paying $7")
	else:
		print("You are paying $12")

else:
	print("Sorry you are too short")
