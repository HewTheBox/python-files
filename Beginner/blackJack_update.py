import random
def SumUP(array):

    if sum(array) == 21 and len(array)==2:
        return 0

    if 11 in array and sum(array) > 21:
        array.remove(11)
        array.append(1)
    return sum(array)


def check(isIn):
    if 11 in isIn:
        index = isIn.index(11)
        num = isIn[index] = 1
        return num
    
def Add(lst):
    num = random.choice(lst)
    return num

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score ==0:
        return "Lose, opponent has Blackjack"
    elif user_score ==0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over you.You win"
    elif computer_score > user_score:
        return "You win"
    else:
        return "You lose"

def playgame():

    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    pc = []

    user = []

    is_game_over = False

    for i in range(2):
        pc.append(Add(cards))
        user.append(Add(cards))

    while not is_game_over:

        user_score = SumUP(user)
        computer_score = SumUP(pc)
        # print(user_score,user)


        print(f"   Your cards: {user}, current score: {user_score}")
        print(f"   Computer's first card: {pc[0]}")

        if user_score ==0 or computer_score ==0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal =="y":
                user.append(Add(cards))
            else:
                is_game_over = True


    while computer_score != 0 and computer_score > 17:
        pc.aappend(Add(cards))
        computer_score = SumUP(pc)


    final = compare(user_score,computer_score)
    print(f"Your final hand: {user}, final score: {user_score}\nComputer's final hand: {pc}, final score: {computer_score}")
    print(final)

restart = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
while restart =="y":
    playgame()
if restart !="y":
    print("Game over")

# print(user_total)
# print(pc_total)



