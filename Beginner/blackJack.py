import random
start = True
while start:
    
    restart = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

    if restart == "n":
        start = False
        print("Game over!")
    else:


        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        f_user = random.choice(cards)
        user = []
        user.append(f_user)

        f_pc = random.choice(cards)
        pc = []
        pc.append(f_pc)


        f_user = random.choice(cards)
        user.append(f_user)
        f_pc = random.choice(cards)
        pc.append(f_pc)

        user_total = 0
        pc_total  = 0

        for i in user:
            user_total+=i

        # for i in pc:
        #     pc_total+=i

        print(f"Your cards {user}, current score: {user_total}\nComputer's first card: {pc[0]}")

        choose_again = input("Do you want another card? 'y' or 'n': ")
        not_greater_than = True
        while choose_again =="y" and not_greater_than:
           
            f_user = random.choice(cards)
            user.append(f_user) 
            user_total =0
            for i in user:
                user_total+=i
            
            print(f"Your cards {user}, current score: {user_total}\nComputer's first card: {pc[0]}")
            if user_total >=21:
                not_greater_than = False
            else:
                choose_again = input("Do you want another card? 'y' or 'n': ")
            
        # else:
        #     print(exit)




        # for i in user:
        #     user_total+=i

        for i in pc:
            pc_total+=i



        while pc_total< 17:
            f_pc = random.choice(cards) 
            pc.append(f_pc)
            pc_total = 0
            for i in pc:
                pc_total+=i



        if user_total > 21:
            print("You loose")
            print(f"Your cards: {user}, current score: {user_total}\nComputer's first card: {pc[0]}")
            print(f"Your final hand: {user}, final score: {user_total}\nComputer's final hand: {pc}, final score: {pc_total}")

        elif pc_total > 21:
            print("You win")
            print(f"Your cards: {user}, current score: {user_total}\nComputer's first card: {pc[0]}")
            print(f"Your final hand: {user}, final score: {user_total}\nComputer's final hand: {pc}, final score: {pc_total}")
        elif user_total == pc_total:
            print("it's  draw")
            print(f"Your cards: {user}, current score: {user_total}\nComputer's first card: {pc[0]}")
            print(f"Your final hand: {user}, final score: {user_total}\nComputer's final hand: {pc}, final score: {pc_total}")
        elif user_total > pc_total:
            print("You win")
            print(f"Your cards: {user}, current score: {user_total}\nComputer's first card: {pc[0]}")
            print(f"Your final hand: {user}, final score: {user_total}\nComputer's final hand: {pc}, final score: {pc_total}")
        else:
            print("You loose")
            print(f"Your cards: {user}, current score: {user_total}\nComputer's first card: {pc[0]}")
            print(f"Your final hand: {user}, final score: {user_total}\nComputer's final hand: {pc}, final score: {pc_total}")

