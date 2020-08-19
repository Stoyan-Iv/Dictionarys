n = int(input())
rarity_dict = {}
rate_dict = {}
for i in range(n):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])
    if plant not in rarity_dict.keys():
        rarity_dict[plant] = []
        rate_dict[plant] = []
    rarity_dict[plant].append(rarity)

command = input()
while command != "Exhibition":
    command = command.split(": ")
    action = command[0]
    plant_info = command[1].split(" - ")
    plant = plant_info[0]
    if plant not in rate_dict.keys():
        print("error")
        command = input()
        continue
    if action == "Rate":
        rate = int(plant_info[1])
        rate_dict[plant].append(rate)
    elif action == "Update":
        new_rerity = int(plant_info[1])
        rarity_dict[plant] = [new_rerity]
    elif action == "Reset":
        rate_dict[plant] = []
    else:
        print(f"error")

    command = input()
avrg_rate_dict = {}
for key, value in rate_dict.items():
    if len(value) >0:
        avrg = sum(value) / len(value)
        avrg_rate_dict[key] = [avrg]
    else:
        avrg_rate_dict[key] = [0]

for key, value in rarity_dict.items():
    avrg_rate_dict[key] += (value)

final_dict = dict(sorted(avrg_rate_dict.items(), key=lambda c: (-c[1][1], -c[1][0])))
print("Plants for the exhibition:")
for key, value in final_dict.items():
    print(f"- {key}; Rarity: {value[1]}; Rating: {value[0]:.2f}")