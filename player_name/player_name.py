import numpy as np
from print_statements import name_prints as p

def stillNotY(yon):
    return not(yon == "y" or yon == "Y")

def validateInput(yon):
    return not(yon == "Y" or yon == "y" or yon == "N" or yon == "n")

def namePlayer():
    yon = ""
    notY = stillNotY(yon)
    
    while(notY):
        p.askName()
        name = input()

        p.confirmName(name)
        yon = input()

        stillInvalid = validateInput(yon)

        while(stillInvalid):
            p.invalidInput()
            yon = input()
            stillInvalid = validateInput(yon)

        if(yon == "n" or yon == "N"):
            p.eneteredN()
        notY = stillNotY(yon)
    return name