dwarf_dic = {}
import collections
counter_dict = collections.defaultdict(int)
while True:
    string = input()
    if string == "Once upon a time":
        break
    name, colore, phisics = string.split(" <:> ")
    phisics = int(phisics)

    if colore not  in dwarf_dic:
        dwarf_dic[colore] = {name: phisics}


    else:
        if name not in dwarf_dic[colore]:
            dwarf_dic[colore][name] = phisics
        else:
            if dwarf_dic[colore][name] < phisics:
                dwarf_dic[colore][name] = phisics

res = []
for k, v in dwarf_dic.items():
    for b, c in v.items():
        res.append([b, c, len(v), k])
res = sorted(res, key=lambda x: (-x[1], -x[2]))

for i in res:
    print(f"({i[3]}) {i[0]} <-> {i[1]}")