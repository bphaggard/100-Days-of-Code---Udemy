from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# no_restart = True
#
# while no_restart:
#     print(logo)
#
#     continue_calc = True
#     num1 = float(input("What's the first number?: "))
#
#     while continue_calc:
#         for key in operations:
#             print(key)
#         operator = input("Pick an operator: ")
#         num2 = float(input("What's the next number?: "))
#         total = operations[operator](num1, num2)
#         print(f"{num1} {operator} {num2} = {total}")
#         another_calc = input(
#             f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ").lower()
#
#         if another_calc == "y":
#             num1 = total
#         else:
#             continue_calc = False

# Another solution
def calculator():
    print(logo)

    continue_calc = True
    num1 = float(input("What's the first number?: "))

    while continue_calc:
        for key in operations:
            print(key)
        operator = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))
        total = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {total}")
        another_calc = input(
            f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ").lower()

        if another_calc == "y":
            num1 = total
        else:
            continue_calc = False
            print("\n" * 20)
            calculator() # Recursion

calculator()