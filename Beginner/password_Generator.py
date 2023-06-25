import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']


print("Welcome to the password Generator!")
nr_letters = int(input("How many leeters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

let = ""
for num in range(1,nr_letters):
	nr = random.randint(0,51)
	let = let + letters[nr]

symb = ""
for sym in range(1,nr_symbols):
	nr = random.randint(0,8)
	symb = symb + symbols[nr]

numb = ""
for num in range(1,nr_numbers):
	nr = random.randint(0,9)
	numb = numb + numbers[nr]

all = let+symb+numb
len = len(all)
final = ""
for i in range(1,len):
	final+=random.choice(all)

print(final)
	


