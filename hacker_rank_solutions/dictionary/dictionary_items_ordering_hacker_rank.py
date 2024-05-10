from collections import OrderedDict


ordered_item_list = OrderedDict()
N = int(input())


for i in range(N):
    item_name, space, item_price = input().rpartition(' ')
    ordered_item_list[item_name] = ordered_item_list.get(item_name, 0) + int(item_price)


for item_name, item_price in ordered_item_list.items():
    print(item_name, item_price)
