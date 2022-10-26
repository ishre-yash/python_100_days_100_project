from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
next = True

while (next):
    option = menu.get_items()
    choice = input(f"What would you like? ({option}): ").lower()
    if choice == 'off':
        next = False
    elif choice == 'report':     
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
