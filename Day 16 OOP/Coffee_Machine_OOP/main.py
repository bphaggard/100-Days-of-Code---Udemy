from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""
1. Print report.
2. Check resources sufficient?
3. Process coins.
4. Check transaction successful?
5. Make Coffee.
"""

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

while machine_on:
    user_input = input(f"What would you like? {menu.get_items()}: ").lower()
    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)