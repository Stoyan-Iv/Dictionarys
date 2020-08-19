num = int(input())
rarity_dict = {}
rating_dict = {}
for i in range(num):
    information = input()
    information = information.split("<->")
    if information[0] not in rarity_dict:
        rarity_dict[information[0]] = int(information[1])
    else:
        rarity_dict[information[0]] = int(information[1])
command = input()
while command != "Exhibition":
    tokens = command.split(": ")
    new_tokens = tokens[1].split(" - ")
    plant = new_tokens[0]
    if plant not in rarity_dict:
        print(f"error")
        command = input()
        continue
    if tokens[0] == "Rate":
        if plant not in rarity_dict:
            print ( f"error" )
            command = input ( )
            continue
        rating = int(new_tokens[1])
        if plant not in rating_dict:
            rating_dict[plant] = []
        rating_dict[plant].append(rating)


    elif tokens[0] == "Update":
        if plant not in rarity_dict:
            command = input ( )
            print ( f"error" )
            continue
        new_rarity = int(new_tokens[1])
        rarity_dict[plant] = new_rarity

    elif tokens[0] == "Reset":
        if plant not in rarity_dict:
            command = input ( )
            print ( f"error" )
            continue

        rating_dict[plant] = []
    else:
        print(f"error")

    command = input()

final_dict_rating = {}
for key, value in rating_dict.items():
    n = 0
    avrg_rating = 0
    if len(value) != 0:
        avrg_rating = (sum(value) / len(value))
    final_dict_rating[key] = [avrg_rating]

for key, value in rarity_dict.items():
    final_dict_rating[key].append(value)


sorted_dict = dict(sorted(final_dict_rating.items(), key= lambda c: (-c[1][1], -c[1][0])))
print(f"Plants for the exhibition:")
for key, value in sorted_dict.items():
    print(f"- {key}; Rarity: {value[1]}; Rating: {value[0]:.2f}")
