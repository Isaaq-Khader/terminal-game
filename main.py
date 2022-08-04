import numpy as np
from player_name import player_name as pn
from print_statements import greeting, introduction
from command_interpreter import command

def main():
    greeting.welcome()
    name = pn.namePlayer()
    introduction.intro(name)

    cmd = ""
    gameIsActive = True

    while(gameIsActive):
        cmd = command.readCommand()
        parseCMD = command.parseCommand(cmd)
        returnCode = command.executeCommand(parseCMD)
        
        gameIsActive = returnCode


    return 0

main()