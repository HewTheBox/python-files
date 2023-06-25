# def format_name(f_name,l_name):
   
#     return f"hello {f_name.title()} {l_name.title()}"

# fName = input("Enter your first name? ")
# lName = input("Enter your last name? ")
# changed_name = format_name(fName,lName)
# print(changed_name)


year  = int(input("Enter a year you want to check? "))
month = int(input("Enter the month"))
def check_leap_year(year):
    if year % 4 ==0:
            if year % 100 ==0:
                    if year % 400 ==0:
                            return True
                    else:
                            return False
            else:
                    return True
    else:
            return False
# print(check_leap_year(year))

def days_in_month(year,month):
    """Take a year and a month to return days"""
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    is_leap = check_leap_year(year)
    if is_leap:
        for i in range(1,len(month_days)):
            if i ==28:
                i +=1
            return month_days[month -1]
    else:
        k = month -1
        return month_days[k]
days = days_in_month(year,month)
print(days)