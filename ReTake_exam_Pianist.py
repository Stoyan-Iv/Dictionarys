my_dict = {}
n = int(input())
for i in range(n):
    piece, composer, klavish = input().split("|")
    my_dict[piece] = [composer, klavish]
command = input()
while command != "Stop":
    tokens = command.split("|")
    action = tokens[0]
    if action == "Add":
        new_piece = tokens[1]
        new_composer = tokens[2]
        new_klavish = tokens[3]
        if new_piece in my_dict.keys():
            print(f"{new_piece} is already in the collection!")
        else:
            my_dict[new_piece] = [new_composer, new_klavish]
            print(f"{new_piece} by {new_composer} in {new_klavish} added to the collection!")

    elif action == "Remove":
        new_piece = tokens[1]
        if new_piece in my_dict:
            my_dict.pop(new_piece)
            print(f"Successfully removed {new_piece}!")
        else:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_piece = tokens[1]
        new_klavish = tokens[2]
        if new_piece in my_dict.keys():
            my_dict[new_piece][1] = new_klavish
            print(f"Changed the key of {new_piece} to {new_klavish}!")
        else:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")


    command = input()

sorted_dict = dict(sorted(my_dict.items(), key= lambda c: (c[0], c[1][0])))
for key, value in sorted_dict.items():
     print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")