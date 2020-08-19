my_dict_price = {}
my_dict_quontiti = {}
stop = False

while True:
    command = input().split(" ")
    if command[0] == "buy":
        stop = True
        break
    product = command[0]
    price = float(command[1])
    quontity = int(command[2])
    if product not in my_dict_price:
        my_dict_price[product] = 0
        my_dict_quontiti[product] = 0
    my_dict_price[product] = price
    my_dict_quontiti[product] += quontity

for key, value in my_dict_price.items():
    print(f"{key} -> {(value * my_dict_quontiti[key]):.2f} ")