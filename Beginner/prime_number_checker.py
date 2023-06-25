def prime_checker(number):
	if number ==2 or number ==3:
		print(f"{number} is a prime number")
	elif number % 2 ==0 or number % 3 ==0:
		print(f"{number} is not a prime number")
	else:
		print(f"{number} is a prime number")

number = int(input("Enter a number: "))
prime_checker(number)
isPrime = True
for i in range(2,number):
	if number % i ==0:
		isPrime = False
if isPrime:
	print("It's prime")
else:
	print("not prime")

