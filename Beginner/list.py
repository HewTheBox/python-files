import random
names_string = input("Enter names ")
names = names_string.split(", ")
number_of_people = len(names)
size = random.randint(0,number_of_people - 1)
per = random.choice(names)
print(per)
print(f"{names[size]} is going to buy the food today")
