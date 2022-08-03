import numpy as np
from player_name import player_name as pn

def greeting():
    print("==============================")
    print("Welcome to the game!")
    print("==============================\n")

def main():
    greeting()

    name = pn.namePlayer()

    print("Alright! Let's get this started.\n\n")


    return 0

main()