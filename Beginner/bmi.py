height = float(input("enter your height "))
weight = float(input("enter your weight "))
bmi  = weight/ (height **2)
if bmi < 18.5:
	print(f"Your BMI is {round(bmi,2)}, you are underweight")
elif bmi < 25:
	print(f"Your BMI is {round(bmi,2)}, you are a normal weight")
elif bmi < 30:
	print(f"Your BMI is {round(bmi,2)}, you are overweight")
elif bmi <35:
	print(f"Your BMI is {round(bmi,2)}, you are obese")
else:
	print(f"Your BMI is above {round(bmi,2)}, you are clinically obese")

