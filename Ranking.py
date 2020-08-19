contest_dict = {}
final_dict = {}
while True:
    contest_and_pasword = input()
    if contest_and_pasword == "end of contests":
        break
    race, abs_pasword = contest_and_pasword.split(":")
    if race not in contest_dict:
        contest_dict[race] = ""
    contest_dict[race] = abs_pasword

while True:
    informatione = input()
    if informatione == "end of submissions":
        break
    contest, password, username, points = informatione.split("=>")
    if contest in contest_dict:
        if password in contest_dict[contest]:
            add_item = [contest, int(points)]
            if username not in final_dict:
                final_dict[username] = []
                final_dict[username].append(add_item)
            elif contest not in final_dict[username][0]:
                final_dict[username].append(add_item)
            else:
                for x in range(len(final_dict[username])):
                    if final_dict[username][x][0] == contest:
                        if final_dict[username][x][1]<= int(points):
                            final_dict[username][x][1] = int(points)
name_biggest = ""
biggest = 0

for key, value in final_dict.items():
    numers = 0
    for val in value:
        a = val[1]
        numers += a
    if biggest < numers:
        biggest = numers
        name_biggest = key
print(f"Best candidate is {name_biggest} with total {biggest} points.")

final_dict= dict(sorted(final_dict.items(), key= lambda x: x[0]))

print(f"Ranking:")
for name in final_dict:
    print(f"{name}")
    for cont, poin in sorted(final_dict[name], key= lambda x: -x[1]):
        print(f"#  {cont} -> {poin}")




