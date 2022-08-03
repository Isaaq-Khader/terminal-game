import numpy as np

def main():
    print("==============================")
    print("Welcome to the game!")
    print("==============================\n")

    yon = ""
    while(yon != "y" or yon != "y"):
        print("What is your name: ", end='')
        res = input()

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


    print("Alright! Let's get this started.\n\n")


    return 0

main()