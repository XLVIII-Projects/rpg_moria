import random
from character import inventory

breakline = "\n" + "-"*30 + "\n"

events = [
    {"You encounter a dead body": {"gold": 3}},
    {"You encounter a chest": {"gold": 2, "food": 1}},
    {"You encounter a golden chest": {"gold": 5}},
]
    
def event(character):
    print(breakline)
    print("You encounter an event!")
    event = random.choice(events)
    for key, value in event.items():
        print(key)
        for k, v in value.items():
            print(f"You find {v} {k}.")
            inventory[k] += v
