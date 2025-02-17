# data = []
#
# with open("weather_data.csv") as weather:
#     for index in weather:
#         values = index.strip()
#         data.append(values)
#
# print(data)

# import csv
#
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     next(data) #exclude header
#     for row in data:
#         temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data.temp) #shows only temp column
#
# data_dict = data.to_dict() #convert to dictionary
# print(data_dict)
#
# temp_list = data.temp.to_list() #convert column values to list
# print(temp_list)

# #Average temperature
# temperature_data = data.temp.to_list()
# average_temp = sum(temperature_data) / len(temperature_data)
# print(average_temp)
#
# #Average with pandas
# print(data.temp.mean())
#
# #Maximum value with pandas
# print(data.temp.max())

# #Show specific row
# print(data[data.day == "Monday"])
#
# #Show row with max temp
# print(data[data.temp == data.temp.max()])

# #Monday temp from Celsius to Fahrenheit
# monday = data[data.day == "Monday"]
# print((monday.temp[0] * 1.8) + 32)

#Create DataFrame
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data") #Create csv file