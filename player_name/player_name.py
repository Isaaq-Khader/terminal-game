import numpy as np
from print_statements import name_prints as p

def namePlayer():
    yon = ""

    notY = not(np.logical_xor(yon != "y", yon != "Y"))
    while(notY):
        p.askName()
        name = input()

        p.confirmName(name)
        yon = input()

        stillInvalid = not(yon == "Y" 
                           or yon == "y" 
                           or yon == "N" 
                           or yon == "n")
        while(stillInvalid):
            p.invalidInput()
            yon = input()

        if(yon == "n" or yon == "N"):
            p.eneteredN()
    return name