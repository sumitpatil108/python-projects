# with open("weather_data.csv") as W:
#     while len(W.readline())!=0:
#         print(W.readline())


# import csv
#
# with open("weather_data.csv") as W:
#     data = csv.reader(W)
#     temp = []
#     for i in data:
#
#         temp.append(i[1])
#         print(i)
# print(temp)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"].max())

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Greay_count = len(data[data["Primary Fur Color"]=="Gray"])
red_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_count = len(data[data["Primary Fur Color"]=="Black"])

dict = {
    "color":["Gray","Cinnamon", "black"],
    "count":[Greay_count, red_count, black_count]
}

df = pandas.DataFrame(dict)
print(df)