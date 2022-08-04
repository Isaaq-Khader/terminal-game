import numpy as np

def readCommand():
    cmd = input()
    return cmd

def parseCommand(cmd):
    parse = cmd.split()
    return parse

def executeCommand(cmd):
    for c in cmd:
        match c:
            case "exit":
                print("exiting!")
                return 0
            case "battle":
                print("let's battle!!!")
                return 1
            case _:
                print("i don't know that command!")
                return 2


