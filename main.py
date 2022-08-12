import numpy as np
from project.player_name import name_player as pn 
from project.print_statements import greeting
from project.command_interpreter import homeCommand
from project.print_statements import introduction

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