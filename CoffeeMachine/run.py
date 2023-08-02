from main import MENU,resources



#resource Checker
def make(type,data):
    """check if resources are enough to prepare a particular coffee. It returns True if resources are enough and returns False if resources are not enough"""
    
    if type =="espresso":
        if  water-MENU["espresso"]["ingredients"]["water"] >=0 and coffee-MENU["espresso"]["ingredients"]["coffee"] >=0:
            return True
        else:
            return False
    elif type =="latte":
        if water-MENU["latte"]["ingredients"]["water"] >=0 and coffee-MENU["latte"]["ingredients"]["coffee"] >=0 and milk-MENU["latte"]["ingredients"]["milk"] >=0:
            return True
        else:
            return False
        
    elif type =="cappuccino":
        if water-MENU["cappuccino"]["ingredients"]["water"] >=0 and coffee-MENU["cappuccino"]["ingredients"]["coffee"] >=0 and milk-MENU["cappuccino"]["ingredients"]["milk"] >=0:
            return True
        else:
            return False


#coin Proccessor
def proccess_coins():
    """Takes coins as input and return the actual money"""
    print("insert coins")
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("Nickles: "))
    pennies = float(input("Pennies: "))
    
    money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return round(money)


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
cost = 0
repeat = True

while repeat:
    
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    ready = make(choice,MENU)


    if choice == "espresso" and ready:
        profit = proccess_coins()
        if profit >=MENU["espresso"]["cost"]:
        
            water-=MENU["espresso"]["ingredients"]["water"]
            coffee-=MENU["espresso"]["ingredients"]["coffee"]
            cost +=MENU["espresso"]["cost"]
        
            if profit > cost:
                profit -=cost
                print(f"Here is ${profit} dollars in change\nHere is your espresso. Enjoy!")
            else:
                print(f"Here is your espresso. Enjoy!")
                
                
        elif profit < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")


    elif choice =="latte" and ready:
        profit = proccess_coins()
        if profit >=MENU["latte"]["cost"]:
            
            water-= MENU["latte"]["ingredients"]["water"]
            milk-= MENU["latte"]["ingredients"]["milk"]
            coffee-= MENU["latte"]["ingredients"]["coffee"]
            cost +=MENU["latte"]["cost"]
        
            if profit > cost:
                profit -=cost
                print(f"Here is ${profit} dollars in change\nHere is your latte. Enjoy!")
            else:
                print(f"Here is your latte. Enjoy!")
                
                
        elif profit < MENU["latte"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")


    elif choice =="cappuccino" and ready:
        profit = proccess_coins()
        
        if profit >=MENU["cappuccino"]["cost"]:
            
            water-= MENU["cappuccino"]["ingredients"]["water"]
            milk-= MENU["cappuccino"]["ingredients"]["milk"]
            coffee-= MENU["cappuccino"]["ingredients"]["coffee"]
            cost +=MENU["cappuccino"]["cost"]
        
            if profit > cost:
                profit -=cost
                print(f"Here is ${profit} dollars in change\nHere is your cappuccino. Enjoy!")
            
            else:
                print(f"Here is your cappuccino. Enjoy!")
                
        elif profit < MENU["cappuccino"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            
            
    elif choice =="report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${round(cost)}")
        
        
    elif not ready and (choice == "espresso" or choice == "latte" or choice == "cappuccino"):
        if water < MENU["latte"]["ingredients"]["water"]:
            print("sorry ther is not enough water")
        elif milk < MENU["latte"]["ingredients"]["milk"]:
            print("sorry there is not enough milk")
        elif coffee < MENU["latte"]["ingredients"]["coffee"]:
            print("sorry there is not enough coffee")
        

    elif choice == "off":
        repeat = False
        print("Coffee Machine Shutdown...")
        
        
    else:
        print("Invalid Input")
        