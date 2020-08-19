n = int(input())
hero_dict = {}
for i in range(n):
    hero_info = input().split(" ")
    hero_name = hero_info[0]
    hp = int(hero_info[1])
    mp = int(hero_info[2])
    hero_dict[hero_name] = [hp, mp]

command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if mp_needed > hero_dict[hero][1]:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
        else:
            hero_dict[hero][1] = hero_dict[hero][1] - mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {hero_dict[hero][1]} MP!")

    elif action == "TakeDamage":
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes_new_hp = hero_dict[hero][0] - damage
        if heroes_new_hp > 0:
            hero_dict[hero][0] = heroes_new_hp
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_new_hp} HP left!")
        else:
            del hero_dict[hero]
            print(f"{hero} has been killed by {attacker}!")
    elif action == "Recharge":
        hero = command[1]
        amaount = int(command[2])
        new_mp = hero_dict[hero][1] + amaount
        if new_mp > 200:
            amaount = 200 - hero_dict[hero][1]
            print ( f"{hero} recharged for {amaount} MP!" )
            hero_dict[hero][1] = 200

        else:
            hero_dict [ hero ] [ 1 ] = new_mp
            print(f"{hero} recharged for {amaount} MP!")
    elif action == "Heal":
        hero = command[1]
        amaount = int(command[2])
        new_hp = hero_dict [ hero ] [ 0 ] + amaount
        if new_hp > 100 :
            amaount = 100 - hero_dict [ hero ] [ 0 ]
            print ( f"{hero} healed for {amaount} HP!" )
            hero_dict [ hero ] [ 0 ] = 100
        else:
            hero_dict [ hero ] [ 0 ] = new_hp
            print ( f"{hero} healed for {amaount} HP!" )


    command = input()
sorted_dict = dict(sorted(hero_dict.items(), key= lambda c: (-c[1][0], c[0])))

for key, value in sorted_dict.items():
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")