import numpy as np
from player_name import player_name as pn
from print_statements import greeting

def main():
    greeting.welcome()
    name = pn.namePlayer()

    print("Alright", name + "!", "Let's get this started.\n\n")


    return 0

main()