import numpy as np
from player_name import player_name as pn
from print_statements import greeting, introduction
from command_interpreter import homeCommand

def main():
    greeting.welcome()
    name = pn.namePlayer()
    introduction.intro(name)

    cmd = ""
    gameIsActive = True

    while(gameIsActive):
        cmd = homeCommand.readCommand()
        parseCMD = homeCommand.parseCommand(cmd)
        returnCode = homeCommand.executeCommand(parseCMD)
        
        gameIsActive = returnCode


    return 0

main()