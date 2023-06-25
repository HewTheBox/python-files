from art import logo,vs
import random
from data import data

#function to generate name,work and country text
def Text(item):
    description = item["description"]
    name = item["name"]
    country = item["country"]
    return f"{name},a {description}, from {country}."

#function for compare returns True or False. Thus, True if Item1 > item2
def compare(item1,item2):
    item1_followers= item1["follower_count"]
    item2_followers= item2["follower_count"]
    if item1_followers > item2_followers:
        return True
    else:
        return False

#evaluate answers
def evaluate_answer(item1,item2,choice):
    answer = ""
    compare_results = compare(item1,item2)

    if compare_results:
        answer = "a"
    else:
        answer = "b"

    #track score
    score = 0
    if choice == answer:
        score += 1
        return answer
    

#function to print comparison
def showText(item1,item2):
    itemA = Text(item1)
    itemB = Text(item2)
    #print comparison
    print(f"Compare A: {itemA}")
    print(vs)
    print(f"Against B: {itemB}")


print(logo)
should_continue = True
score = 0
list2 = random.choice(data)
while should_continue:
    LISTS  = data
    list1 = list2
    list2 = random.choice(LISTS)
    index1 = LISTS.index(list1)
    index2 = LISTS.index(list2)
    # random_generate = choice(LISTS)

    if list1 == list2:
        list2 = random.choice(LISTS)
    showText(list1,list2)
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    results = evaluate_answer(list1,list2,choice)
    # new_list = {}
    repeat = False
    
    if results =="a" or results =="b":
        score+=1
        list1 = list2
        print(f"You're right! Current score: {score}.")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")


