student_scores = input("Input a list of student score ").split()
for n in range(0, len(student_scores)):
	student_scores[n] = int(student_scores[n])

max = 0
for big in student_scores:
	if big >max:
		max = big
min = 200
for small in student_scores:
	if small < min:
		min = small

print(f"The heighest score is {max} and the lowest score is {min}")

