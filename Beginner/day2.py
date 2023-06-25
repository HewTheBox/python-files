print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? "))
tip_in_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people are to split the bill? "))

tip = (tip_in_percent / 100) * total_bill
# current_bill = total_bill + tip
total_bill = total_bill +  tip
result = total_bill / number_of_people
print(f"Each person should pay : {round(result,2)}")
print(round(result,2))

