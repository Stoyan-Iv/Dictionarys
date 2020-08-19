like_dict = {}
command = input()
unlike_count = 0
while command != "Stop":
    tokens = command.split("-")
    process = tokens[0]
    guest = tokens[1]
    meal = tokens[2]
    if process == "Like":
        if guest not in like_dict:
            like_dict[guest] = []
        if meal not in like_dict[guest]:
            like_dict[guest].append(meal)
    elif process == "Unlike":
        if guest not in like_dict:
            print(f"{guest} is not at the party.")
        elif meal not in like_dict[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            unlike_count += 1
            like_dict[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
    command = input()

sorted_dict = dict(sorted(like_dict.items(), key = lambda c: (-len(c[1]), c[0])))

for key, value in sorted_dict.items():
    print(f"{key}: {', '.join(value)}")
print(f"Unliked meals: {unlike_count}")