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

# Basic Settings#

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

# Mode Settings #
def setmodewasd():
    mode = definitions.player.stats["mode"]
    definitions.player.stats["mode"] = "WASD"
    print("Mode changed to WASD")

def setmodetxt():
    mode = definitions.player.stats["mode"]
    definitions.player.stats["mode"] = "TXT"
    print("Mode changed to TXT")


# Settings command
def settings():
        choice = input("""
        Player Settings:
        cn -- Character Name
        cs -- Ship Name
        Game Settings:
        wm -- WASD mode for controlling ship
        tm -- TEXT mode for controlling ship
        >> """)
        if choice in ["cn","name","NAME"]:
            setname()
        elif choice in ["csn","cs","shipname","SHIPNAME"]:
            setshipname()
        elif choice in ["wm","WASD","wasd","WM"]:
            setmodewasd()
            commands.command()
        elif choice in ["tm","TXT","txt","TM"]:
            setmodetxt()
            commands.command()