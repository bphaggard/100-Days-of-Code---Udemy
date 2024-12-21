name = input("Name: ")
surname = input("Surname: ")


# def format_name(f_name, l_name):
#     return f"{f_name.title()} {l_name.title()}" # title() set first letter to Upper letter
#
# print(format_name(name, surname))
#
# def function_1(text):
#     return text + text
#
# def function_2(text):
#     return text.title()
#
# output = function_2(function_1("hello"))
# print(output) # Hellohello

# Multiple return values
def format_name(f_name, l_name):
    """Take a first and last name and format it to
    return the title case version of the name"""  #Docstring (information about function)
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    return f"{f_name.title()} {l_name.title()}"


print(format_name(name, surname))
