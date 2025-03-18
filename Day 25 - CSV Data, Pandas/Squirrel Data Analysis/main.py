import pandas

data = pandas.read_csv("2018_Squirrel_Data.csv")

grey = 0
red = 0
black = 0

for item in data["Primary Fur Color"]: #data["Primary Fur Color"] show specific column
    if item == "Gray":
        grey += 1
    elif item == "Cinnamon":
        red += 1
    elif item == "Black":
        black += 1

# #Simplify
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_squirrel_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
# }

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey, red, black]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count")