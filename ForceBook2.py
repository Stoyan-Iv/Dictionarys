my_dict = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if " | " in command:
        args = command.split(" | ")
        forse_side = args[0]
        forse_user = args[1]
        all_values = []
        for list in my_dict.values():
            all_values += list
        if forse_side not in my_dict:
            my_dict[forse_side] = []
        if forse_user not in all_values:
            my_dict[forse_side].append(forse_user)
        all_values = []

    else:

        args = command.split( " -> " )
        user = args[0]
        side = args[1]
        if side not in my_dict:
            my_dict[side] = []
        for key, value in my_dict.items():
            if user in value:
                my_dict[key].remove(user)

        my_dict[side].append(user)
        print(f"{user} joins the {side} side!")

my_dict = dict(sorted(my_dict.items(), key= lambda x: (-len(x[1]), x[0])))

for key, value in my_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for usersite in sorted(value):
            print(f"! {usersite}")


