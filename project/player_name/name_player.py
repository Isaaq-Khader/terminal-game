import numpy as np
from project.print_statements import name_prints as p

def stillNotY(yon):
    return not(yon == "y" or yon == "Y")

def validateInput(yon):
    return not(yon == "Y" or yon == "y" or yon == "N" or yon == "n")

def getName():
    name = input(p.askName())
    return name

def getYoN(name):
    confirmName, ynConfirm = p.confirmName(name)
    print(confirmName)
    yon = input(ynConfirm)
    return yon

def checkValidity():
    yon = input(p.invalidInput())
    stillInvalid = validateInput(yon)
    return [yon, stillInvalid]

def namePlayer():
    yon = ""
    notY = stillNotY(yon)
    
    while(notY):
        name = getName()
        yon = getYoN(name)
        stillInvalid = validateInput(yon)

        while(stillInvalid):
            yon, stillInvalid = checkValidity()

        if(yon == "n" or yon == "N"):
            print(p.eneteredN())
        notY = stillNotY(yon)
    return name