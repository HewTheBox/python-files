heights = input("Inputs a list of students heights ").split()
i = 0
sum = 0
for n in range(0,len(heights)):
	i+=1
	heights[n] =int(heights[n])
	sum+=heights[n]


result = sum / i
print(round(result))
	
