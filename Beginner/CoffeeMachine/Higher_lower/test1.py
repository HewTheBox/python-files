
repeat = False
counter= 1
while repeat or counter > 0:
    from art import logo,vs
    from random import randint,choice
    from data import data
    repeat = False


    #declaring global variables
    LISTS  = data
    list1 = choice(LISTS)
    list2 = choice(LISTS)
    index1 = LISTS.index(list1)
    index2 = LISTS.index(list2)


    #function to generate name,work and country text
    def Text(item):
        description = item["description"]
        name = item["name"]
        country = item["country"]
        return f"{name},a {description}, from {country}."

    #function for compare
    def compare(item1,item2):
        item1_followers= item1["follower_count"]
        item2_followers= item2["follower_count"]
        if item1_followers > item2_followers:
            return True
        else:
            return False


    #Storing name,work and country information
    itemA = Text(list1)
    itemB = Text(list2)

        
    #print comparison
    print(f"Compare A: {itemA}")
    print(vs)
    print(f"Against B: {itemB}")

    #asking user for answer
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()




    #evaluate answer
    answer = ""
    new_item = ""
    list3 = {}
    follow_count = 0

    if compare(list1,list2):
        answer = "a"
        new_item = itemA
        list3 = list1
    else:
        answer = "b"
        new_item = itemB
        list3 = list2


    #track score
    score = 0
    if choice == answer:
        score+=1
    if score > 0:
        print(f"Your score is {score}")
        repeat = True

    counter-=1


    

