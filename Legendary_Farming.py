
my_dict = {}
quontiti = []
material = []
final_dict = {}
finish = False

while True:
    string = input().split( " " )
    for i in range( len( string ) ):
        if i % 2 == 0:
            quontiti.append( string[i] )
        else:
            asd = string[i].lower()
            material.append( asd )
    for i in range(len(material)):
        quint = quontiti[i]
        mat = material[i]

        if mat not in my_dict:
            my_dict[mat] = 0
        my_dict[mat] += int(quint)

        if mat == "shards":
            if my_dict["shards"] >= 250:
                finish = True
                print(f"Shadowmourne obtained!")
                my_dict["shards"] -= 250
        if mat == "fragments":
            if my_dict["fragments"] >= 250:
                finish = True
                print(f"Valanyr obtained!")
                my_dict["fragments"] -= 250
        if mat == "motes":
            if my_dict["motes"] >= 250:
                print(f"Dragonwrath obtained!")
                my_dict["motes"] -= 250
                finish = True


        if finish == True:
            break

final_dict = my_dict.copy()
kraen = {}
for key, value in final_dict.items():
    if  key != "shards" and key != "fragments" and key != "motes":
        my_dict.pop(key)
        kraen[key] = value

sorted_my_dict = dict(sorted(my_dict.items(), key=lambda x:(-x[1], x[0])))
for key, value in sorted_my_dict.items():
    print(f"{key}: {value}")
sorted_kraini = dict(sorted(kraen.items(), key=lambda x: (x[0]) ))
for key, value in sorted_kraini.items():
    print(f"{key}: {value}")

