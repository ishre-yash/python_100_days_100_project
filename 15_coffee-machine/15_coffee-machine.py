import os
MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk": 0,
                "coffee": 18,
            },
            "cost": 100,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 200,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 300,
        }
    }
    
resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }
def report(resources):
    print(f"💧Water: {resources['water']}ml")
    print(f"🥛Milk: {resources['milk']}ml")
    print(f"☕Coffee: {resources['coffee']}g")
    print(f"💲Money: ₹{resources['money']}")
    
def checkResources(choice):
    if resources['water'] >= MENU[choice]['ingredients']['water']:
        if resources['coffee'] >= MENU[choice]['ingredients']['coffee']:
            if resources['milk'] >= MENU[choice]['ingredients']['milk']:
                return True
    return False
    
def checkMoney(choice, resources):
    print("Please insert coins/ bills.")
    ten = int(input("how many ₹10 coins : "))
    fifty = int(input("how many ₹50 Bills:"))
    hundred = int(input("how many ₹100 Bills:"))
    total = (ten * 10)+(fifty * 50)+(hundred * 100)
    if total < MENU[choice]['cost']:
        print(f"Sorry that's not enough money. Money refunded: ₹{total}")
    elif total >= MENU[choice]['cost']:
        total -= MENU[choice]['cost']
        print(f"Here is {total} rupee in change.")
        print(f"Here is Your {choice} ☕. Enjoy!")
        resources['water'] -= MENU[choice]['ingredients']['water']
        resources['milk'] -= MENU[choice]['ingredients']['milk']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']
        resources['money'] += MENU[choice]['cost']
        
print("Type :\n📄'menu' to see MENU \n🔁'report' to see report\n📴'off' to turn off the Coffee Machine")
next = True
while (next):
    choice = input("What would you like? (espresso/latte/cppuccino): ").lower()
    if choice == 'off':
        next = False
        os.system('clear')
    elif choice == 'report':
        os.system('clear')
        report(resources)
    elif choice == 'menu':
        os.system('clear')
        print(f"Price:🏷️\n🍵Espresso: ₹{MENU['espresso']['cost']}\n☕Latte: ₹{MENU['latte']['cost']}\n🥡Cappuccino: ₹{MENU['cappuccino']['cost']}\n")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
       if MENU[choice]:
            check = checkResources(choice)
            if check == False:
                os.system('clear')
                print("Sorry there is not enough water.\n\n")
            else:
                checkMoney(choice, resources)
    else:
        os.system('clear')
        print("Type correct name before enter...")