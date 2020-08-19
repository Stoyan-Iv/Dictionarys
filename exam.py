num_cars = int(input())
cars_dict = {}
for i in range(num_cars):
    car, mileage, fuel = input().split("|")
    cars_dict[car] = [int(mileage), int(fuel)]
while True:
    command = input()
    if command == "Stop":
        break
    command = command.split(" : ")
    if command[0] == "Drive":
        curent_car = command[1]
        distance = int(command[2])
        curent_fuel = int(command[3])
        if cars_dict[curent_car][1] >= curent_fuel:
            cars_dict[curent_car][0] += distance
            cars_dict[curent_car][1] -=curent_fuel
            print(f"{curent_car} driven for {distance} kilometers. {curent_fuel} liters of fuel consumed.")
        else:
            print(f"Not enough fuel to make that ride")
        if cars_dict[curent_car][0] >= 100000:
            print(f"Time to sell the {curent_car}!")
            cars_dict.pop(curent_car)

    elif command[0]== "Refuel":
        curent_car = command[1]
        curent_fuel = int( command[2] )
        if cars_dict[curent_car][1] + curent_fuel > 75:
            print(f"{curent_car} refueled with {75 - cars_dict[curent_car][1] } liters")
            cars_dict[curent_car][1] = 75
        else:
            cars_dict[curent_car][1] += curent_fuel
            print( f"{curent_car} refueled with {curent_fuel} liters" )
    elif command[0] == "Revert":
        curent_car = command[1]
        kilometre = int( command[2] )
        cars_dict[curent_car][0] -= kilometre
        if cars_dict[curent_car][0] < 10000:
            cars_dict[curent_car][0] = 10000
        else:
            print(f"{curent_car} mileage decreased by {kilometre} kilometers")

sorted_cars = dict(sorted(cars_dict.items(), key=lambda c: (- c[1][0],c[0])))

for key, value in sorted_cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")