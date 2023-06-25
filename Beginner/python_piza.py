price = 0

size = input("Enter pizza size ")
want_pepperoni = input("Do you want pepperoni? ")
extra_cheese = input("Do you want extra cheese? ")


if size == "S":
	price =15
	print(f"Price of small Pizza is ${price}.")
elif size =="M":
	price = 20
	print(f"Price of medium pizza is ${price}.")
elif size =="L":
	price= 25
	print(f"Price of Large pizza is ${price}.")
else:
	print("Wrong Choice")
if want_pepperoni =="Y":
	if size == "S":
		price+=2
	else:
		size+=3
#else:
	#print("No pepperoni")

if extra_cheese == "Y":
	price+=1
	print(f"Your final bill is {price}")
else:
	print(f"Your final bill is ${price}")
