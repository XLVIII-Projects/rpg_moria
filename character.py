def create_character():
    name = input("What is your name? Type your answer: ")

    character = {
        "name": name,
        "race": "Dwarf",
        "max hp": 10,
        "hp" : 10,
        "mana": 5,
        "rest_counter": 0,
    }

    return character



inventory = {
    "equipped_weapon": "dagger",
    "equipped_armor": "leather",
    "weapons": ["dagger", "sword", "bow"],
    "armor": ["leather", "chainmail", "plate"],
    "potion": 1,
    "wood": 0,
    "food": 1,
    "gold": 3
}

item_properties = {
        "dagger": {
            "damage": 1
        },
        "sword": {
            "damage": 2
        },
        "bow": {
            "damage": 3
        },
        "leather": {
            "defense": 1
        },
        "chainmail": {
            "defense": 2
        },
        "plate": {
            "defense": 3
        },
        "potion": {
            "healing": 5
        }
    }

    
