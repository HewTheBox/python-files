name1 = input("Enter your name? ")
name2 = input("Enter their name? ")
full_name = (name1 + name2).lower()
a = full_name.count("t")
a +=full_name.count("r")
a +=full_name.count("u")
a +=full_name.count("e")
b =full_name.count("l")
b +=full_name.count("o")
b +=full_name.count("v")
b +=full_name.count("e")
c = str(a) +str(b)
result = int(c)

if result <10 or result>90:
	print(f"Your score is {result}, You go together like coke and mentos")
elif result >=40 and result <=50:
	print(f"Your score is {result}, you are alright together")
else:
	print(f"Your score is {result}.")



