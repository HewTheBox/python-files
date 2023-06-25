bid_Again = True
bids = {}
while bid_Again:

    name = input("What is your name? ")
    price = int(input("What's is your bid? $"))
    bids[name] = price
    check = input("is there another bidder 'yes' or 'no' ").lower()
    if check == "no":
        bid_Again = False

    def who_is_Winning(bids):
        max = 0
        person = 0
        for people in bids:
            if bids[people] > max:
                max = bids[people]
                person = people
        print(f"The highest bidder is {person} with ${max}")

who_is_Winning(bids)

print(bids)  