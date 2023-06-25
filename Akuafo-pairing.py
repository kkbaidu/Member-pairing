
import json

with open('members.json') as members:
    my_list = json.load(members)

print(my_list[::2])

print(my_list[1::2])

result = [item_1 +' and '+ item_2 for item_1, item_2 in zip(my_list[::2], my_list[1::2])]

print(result)