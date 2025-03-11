import random

enemy_list2 = [
    {
        "enemy": "goblin",
        "hp": 5,
        "damage": 2,
        "level": 1,
        "loot": {"gold": 1, "wood": 1}
    },
    {
        "enemy": "orc",
        "hp": 10,
        "damage": 4,
        "level": 2,
        "loot": {"gold": 2, "wood": 2}
    }]

enemylist = []

def create_enemy():
    enemy_adjective = ["Armored ", "Bloodthirsty ", "Radiant ", "Poisonous "]
    enemy_race = ["rat ", "slime ", "slug ", "mosquito ", "spider ", "bat "]
    enemy_type = ["abomination", "amputee", "soldier", "screamer", "stalker", "wraith"]

    enemy_name = random.choice(enemy_adjective) + random.choice(enemy_race) + random.choice(enemy_type)
    
    enemy = {
        "name": enemy_name,
        "hp": 3,
        "damage": 3
    }
    
    enemylist.append(enemy)   