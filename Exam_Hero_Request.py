hero_dict = {}
command = input()
while command != "End":
    tokens = command.split(" ")
    hero_command = tokens[0]
    hero_name = tokens[1]
    if hero_command == "Enroll":
        if hero_name in hero_dict:
            print(f"{hero_name} is already enrolled.")
        else:
            hero_dict[hero_name] = []

    elif hero_command == "Learn":
        spell_name = tokens[2]
        if hero_name not in hero_dict:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in hero_dict[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            hero_dict[hero_name].append(spell_name)

    elif hero_command =="Unlearn":
        spell_name = tokens[2]
        if hero_name not in hero_dict:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in hero_dict[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            hero_dict[hero_name].remove(spell_name)

    command = input ( )

sorted_dict = dict(sorted(hero_dict.items(), key= lambda c: (-len(c[1]), c[0])))


print(f"Heroes:")
for key, value in sorted_dict.items():
        value = ", ".join ( value )

        print(f"== {key}: {value}")



