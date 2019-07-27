#####################
### Basic Imports ###
#####################
import random
######################
### Custom Imports ###
######################
from . import definitions
from . import classes
from . import help 
from . import commands
######################


def setname(): # Set your characters name
    name = input("What is your name captain?\n>>  ")
    print(f"Welcome aboard Captain {name}")

def setshipname(): # Set ship name

    shipname = input("What shall we call your ship?\n>>  ")
    if len(shipname) <= 2:
        shnm = random.sample(["Deluxe","Voltage","Titan"],1)
        definitions.status.status["shipname"] = 'S.S.'.join(shnm)
    else:
        definitions.status.status["shipname"] = shipname
    print(f"Captain Your ship name is set to {definitions.status.status['shipname']}")
    commands.command()