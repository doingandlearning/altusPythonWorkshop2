from itertools import groupby
from operator import itemgetter

data = [("apple", "fruit"), ("banana", "fruit"), ("tomato", "fruit"),
        ("carrot", "vegetable"), ("potato", "vegetable")]


# print(list(groupby(data, key=itemgetter(1))))
def find_category(food):
    return food[1]

for key, group in groupby(data, lambda food: food[1]):
  print(f"{key}: {[item[0] for item in group]}")

for key, group in groupby(data, find_category):
    print(f"{key}: {[item[0] for item in group]}")