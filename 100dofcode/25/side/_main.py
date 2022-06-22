import pandas

data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

data_pfc = data["Primary Fur Color"].to_list()

data_pfc_no_duplicates = list(dict.fromkeys(data_pfc))

main_dictionaries_list = []
colors = []
amounts = []

for color in data_pfc_no_duplicates:

    color_amount = 0

    for color_duplicates in data_pfc:

        if color == color_duplicates:
            color_amount += 1

    new_dict = {f"{color}": color_amount}
    main_dictionaries_list.append(new_dict)

    colors.append(color)
    amounts.append(color_amount)

pandas_dict = {
    "colors": colors,
    "amounts": amounts
}

pandas.DataFrame(pandas_dict).to_csv("squirrels.csv")

# weatherlist = []
# with open("weather_data.csv") as weather:
#     for line in weather:
#         modifiedline = line.strip()
#         weatherlist.append(modifiedline)
# print(weatherlist)

# import csv
#
# temperaturelist = []
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#
#     for row in data:
#         if row[1] != "temp":
#             temperaturelist.append(int(row[1]))
#
#     print(temperaturelist)

# data = pandas.read_csv("./weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temperature_list = data["temp"].to_list()

# print(sum(temperature_list)/len(temperature_list))

# print(data.temp.max())

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# print(f"{data.temp.to_list()[0] * 9/5 + 32}F")

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# pandas.DataFrame(data_dict).to_csv("scores.csv")
