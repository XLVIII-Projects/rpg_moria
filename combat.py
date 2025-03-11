from enemy import enemylist
from character import item_properties, inventory
import random

breakline = "\n" + "-"*30 + "\n"

def enemy_attack(enemy):
    enemy_damage = random.randint(enemy['damage']-2, enemy['damage']+2) 
    blocked = random.randint(item_properties[inventory["equipped_armor"]]["defense"]-1, item_properties[inventory["equipped_armor"]]["defense"]+1)   
    enemy_damage -= blocked
    if enemy_damage < 0:
        enemy_damage = 0
    return enemy_damage, blocked

def character_attack(character):
    character_damage = random.randint(item_properties[inventory["equipped_weapon"]]["damage"]-1, item_properties[inventory["equipped_weapon"]]["damage"]+1)
    return character_damage

def combat(character):
    print(breakline)
    enemy = enemylist[0]
    enemy["hp"] = random.randint(1, 5)

    print(f"You encounter a(n) {enemy["name"]} (enemy hp: {enemy["hp"]})\n")

    while character['hp'] > 0 and enemy['hp'] > 0:
        action = input("Do you attack (a), heal (h) or run (r)? Type your answer: ")
        if action == "a": # attack
            print(breakline)
            character_damage = character_attack(character)
            enemy["hp"] -= character_damage
            print(f"You attack the enemy, dealing {character_damage} damage. Remaining enemy hp: {enemy["hp"]}")
            if enemy["hp"] > 0:
                enemy_damage, blocked = enemy_attack(enemy)
                character["hp"] -= enemy_damage
                print(f"The enemy retaliates dealing {enemy_damage} damage ({blocked} blocked). Remaining hp: {character["hp"]}")
        elif action == "h": # heal
            print(breakline)
            if inventory["potion"] == 0:
                print("You have no potions.")
            if inventory["potion"] > 0:
                print("You drink a potion.")
                character["hp"] += item_properties["potion"]["healing"]
                inventory["potion"] -= 1
                print(f"\nYou now have {inventory["potion"]} potions and {character["hp"]} hp")
        elif action == "r": # run
            print(breakline)
            print("\nYou ran away!")
            return 
    
    if character["hp"] <= 0:
        print(breakline)
        print("You died!")
        return
    else:
        print(breakline)
        print("You defeated the enemy! \n")
        inventory["gold"] += 1
        print(f"You now have {inventory["gold"]} gold.")
        return