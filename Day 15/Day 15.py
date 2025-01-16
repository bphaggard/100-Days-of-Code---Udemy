from data import MENU, resources

"""
Penny = 1 cent = 0.01
Nickel = 5 cents = 0.05
Dime = 10 cents = 0.10
Quarter = 25 cents = 0.25
"""

def wallet(qua, dim, nic, penn):
    """Counts users money."""
    summary = 0.25 * qua + 0.10 * dim + 0.05 * nic + 0.01 * penn
    return summary

def report():
    """Shows how many resources left."""
    for key, value in resources.items():
        if key == "coffee":
            print(f"{key.capitalize()}: {value}g")
        else:
            print(f"{key.capitalize()}: {value}ml")
    print(f"Money: ${user_money}")

def resources_check(coffee):
    """Check resources for ordered coffee."""
    requirements = MENU[coffee]["ingredients"]
    for item, amount in requirements.items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def transaction(coffee):
    requirements = MENU[coffee]["cost"]
    if user_money >= requirements:
        change = round(user_money - requirements, 2)
        global profit
        profit += requirements
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

machine_on = True
user_money = 0
profit = 0

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        report()
    else:
        drink = MENU[user_choice]
        if resources_check(user_choice):
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            user_money = wallet(quarters, dimes, nickles, pennies)
            if transaction(user_choice):
                make_coffee(user_choice, drink["ingredients"])