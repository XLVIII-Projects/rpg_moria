import time
import random
from character import create_character
from enemy import create_enemy
from gameloop import gameloop

def main():
    character = create_character()
    create_enemy()
    gameloop(character)


if __name__ == "__main__":
    main()



