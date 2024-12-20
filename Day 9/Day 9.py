programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}
print(programming_dictionary["Loop"])
programming_dictionary["Error"] = "Bug in a program" # Adding items to dictionary, it`s same if you want to edit item

programming_dictionary = {} # Delete all items in dictionary
print(programming_dictionary)

# Loop

for key in programming_dictionary:
    print(key) # Show only key and not key: value
    print(programming_dictionary[key])

# value in dictionary can be list and dictionary ("France": ["city1", "city2", "city3"])

travel = {
    "France": ["city1", "city2", "city3"],
    "Germany": ["city1", "city2", "city3"]
}
print(travel["France"][1]) # Output is city2
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1]) # Output is D

travel_europe = {
    "France": {
        "cities_visited": ["city1", "city2", "city3"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["city1", "city2", "city3"],
        "total_visits": 5
    }
}
print(travel_europe["Germany"]["cities_visited"][2])