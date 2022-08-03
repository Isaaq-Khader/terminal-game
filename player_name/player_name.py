import numpy as np

def namePlayer():
    yon = ""
    while(yon != "y" or yon != "y"):
        print("What is your name: ", end='')
        name = input()

        print("Your name is", res, "is that correct?")
        print("(Y/N): ", end='')
        yon = input()

        notN = np.logical_xor(yon != "n", yon != "N")
        notY = np.logical_xor(yon != "y", yon != "Y")
        notYoN = notN and notY

        while(notYoN):
            print("(Y/N)?: ", end='')
            yon = input()
        if(yon == "n" or yon == "N"):
            print("\nOkay! Let's change it.")
    return name