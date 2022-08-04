import numpy as np
from player_name import player_name as pn
from print_statements import greeting, introduction, name_prints

def main():
    greeting.welcome()
    name = pn.namePlayer()
    introduction.intro(name)

    return 0

main()