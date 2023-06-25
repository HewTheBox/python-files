another_bider = True
people = []
name =""
amount =0
while another_bider:

    name = input("What is your name\n")
    amount = int(input("How much do you want to bid\n$ "))
    bid_again = input("Is there another bider? 'yes' or 'no'\n").lower()
    
    people1={
        "Name": name,
        "Amount": amount,
    }
    people.append(people1)

    if bid_again == "no":
        another_bider = False


def heighest_bider():
    max = 0
    index = 0
    person = ""
    for i in range(0,len(people)):
        items = people[i]
        money = items["Amount"]
        if money > max:
            max = money
            index = i
            thing = people[index]
            person = thing["Name"]

    print("The person with the highest bid is " +person + str(max))
    

heighest_bider()


# again = [{
#     'Name': 'adsfasdf',
#     'Amount': 444
# }, 
# {
#     'Name': 'gfdhd',
#     'Amount': 66
# },
# {
#     'Name': 'fdgret',
#     'Amount': 798
# }]
# # first = again[0]
# # print(first["Amount"])
# okay = 0
# counter = 0
# for i in range(0,len(again)):

#     first = again[i]
#     if first["Amount"]>okay:
#         okay = first["Amount"]
#         counter = i
# print(okay,counter)
