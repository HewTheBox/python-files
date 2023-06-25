import math
def calc(height,width,coverage):
	area = height * width
	cans = area/coverage
	print(f"You will need {math.ceil(cans)} cans of paint")
height = int(input("Height of wall? "))
width= int(input("Width of wall? "))
coverage = 5

calc(height,width,coverage)

