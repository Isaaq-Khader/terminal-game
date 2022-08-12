import numpy as np
from print_statements import name_prints as p

def stillNotY(yon):
    return not(yon == "y" or yon == "Y")

def validateInput(yon):
    return not(yon == "Y" or yon == "y" or yon == "N" or yon == "n")

def getName():
    p.askName()
    name = input()
    return name

def getYoN(name):
    p.confirmName(name)
    yon = input()
    return yon

def checkValidity():
    p.invalidInput()
    yon = input()
    stillInvalid = validateInput(yon)
    return stillInvalid

def namePlayer():
    yon = ""
    notY = stillNotY(yon)
    
    while(notY):
        name = getName()
        yon = getYoN(name)
        stillInvalid = validateInput(yon)

        while(stillInvalid):
            stillInvalid = checkValidity()

        if(yon == "n" or yon == "N"):
            p.eneteredN()
        notY = stillNotY(yon)
    return name