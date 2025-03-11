from combat import combat
from character import inventory
from events import event
import random


breakline = "\n" + "-"*30 + "\n"

def gameloop(character):
    # base junction
    print(breakline)
    print("You are in a dungeon.\n")
    print("1. Check your inventory.")
    if character["rest_counter"] > 0:
        print(f"2. Head further into the dungeon. You have {character["hp"]} hp and you feel slightly tired.")
    if character["rest_counter"] == 0:
        print(f"2. Head further into the dungeon. You have {character["hp"]} hp and you feel well rested.")
    print(f"3. Set up camp. You have {inventory["wood"]} wood and {inventory["food"]} food.")
    action = input("Choose (1), (2) or (3): ")
    if action == "1": # check inventory
        print(breakline)
        print("You check your inventory. \n")
        print(f"Your inventory: {inventory} \n")
        print("1. Go back.")
        action = input("Choose (1): ")
        if action == "1":
            gameloop(character)
        else:
            print("\nWrong input!")
            gameloop(character)
    elif action == "2": # head further into the dungeon
        random_event = random.choice(["combat", "event", "exploration"])
        if random_event == "combat": # combat
            combat(character)
            print("You survived combat and feel slightly tired")
            character["rest_counter"] += 1
        if random_event == "event": # event
            event(character)     
        if random_event == "exploration": # exploration
            print(breakline)
            print("You explore further into the dungeon.")  
        gameloop(character)
    elif action == "3": # set up camp
        camp(character)

def camp(character):
    print(breakline)
    print("You set up camp and rest. What do you want to do? Type your answer: ")
    print("1. Change your inventory.")
    print("2. Cook food.")
    print("3. Rest.")
    print("4. Go back.")
    action = input("Choose (1), (2), (3) or (4): ")
    if action == "1": # change inventory
        print(breakline)
        print("You check your inventory.\n")
        print(f"Your character: {character} \n")
        for i in inventory:
            if isinstance(inventory[i], list):
                print(f"{i}:")
                for j in inventory[i]:
                    print(f"- {j}")     
            else:
                print(f"{i}: {inventory[i]}")                   
        print("\n")
        print("1. Change your weapon.")
        print("2. Change your armor.")
        print("3. Go back.")
        action = input("Choose (1), (2) or (3): ")
        if action == "1": # change weapon
            print(breakline)
            print("Choose your weapon:\n")
            for weapon in inventory["weapons"]:
                print(weapon)
            weapon = input("\nType your answer: ")
            inventory["equipped_weapon"] = weapon
            print(f"\nYou now have {inventory["equipped_weapon"]} equipped.")
            camp(character)
        if action == "2": # change armor
            print(breakline)
            print("Choose your armor:")
            for armor in inventory["armor"]:
                print(armor)
            armor = input("Type your answer: ")
            inventory["equipped_armor"] = armor
            print(f"\nYou now have {inventory["equipped_armor"]} equipped.")
            camp(character)
        if action == "3": # go back
            camp(character)
        else:
            print(breakline)
            print("Wrong input!")
            camp(character)
    elif action == "2": # cook food
        print(breakline)
        if inventory["food"] == 0:
            print("You have no food to cook.")
            camp(character)
        print("You cook food.")
        inventory["food"] -= 1
        character["hp"] += 1
        print(f"\nYou eat and regain 1 hp.")
        print(f"\nYou now have {inventory["food"]} food and {inventory["gold"]} gold.")
        camp(character)
    elif action == "3": # rest
        print(breakline)
        if character["rest_counter"] == 0:
            print("You don't feel tired.")
            camp(character)
        print("You rest and regain 1 hp.")
        character["rest_counter"] -= 1
        character["hp"] += 1
        print(f"\nYour hp is now {character["hp"]}")
        camp(character)
    elif action == "4": # go back
        gameloop(character)
    else:
        print("\nWrong input!")
        camp(character)