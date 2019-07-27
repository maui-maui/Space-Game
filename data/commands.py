#####################
### Basic Imports ###
#####################
import os
import time
import sys
######################
### Custom Imports ###
######################
from data.help import * 
######################

#Input command function
def command():
    commands = input("COMMAND >> ")
#########################################################################
########################## Help Commands ################################
#########################################################################
    if commands in ["help","?"]:
        help.helpcommand()
    elif commands in ["? map","help map"]:
        help.helpmap()
    elif commands in ["? move","help move"]:
        help.helpmove()
#########################################################################
########################## Control Commands #############################
#########################################################################
    elif commands in ["warp","w","WARP","W"]:
        warpcommand()
    elif commands in ["move","mv"]:
        movecommand()
    elif commands in ["map","m"]:
        mapcommand()
        command()
    elif commands in ["stats","status","ss"]:
        playerchart()
        command()

#########################################################################
######################### Game SYS ######################################
#########################################################################
    elif commands in ['set',"SET","settings","SETTINGS"]:
        settings.settings()
    elif commands in ["clean","clear","cls","clr"]:
        os.system("clear")
        command()
    elif commands in ["exit","quit","x","X","q","Q"]:
        print("Exiting Game...")
        confirm = input("Are you sure you want to exit?\n(Y/N)>> ")
        if confirm in ["y","Y","yes","YES"]:
            print("Game Shutting down...")
            time.sleep(1)
            sys.exit()
        else:
            command()
    else:
        print("Wrong Input! Try again.")
        helpprompt = input("Want to see the help command? (Y/N)\n")
        if helpprompt in ["yes",'YES',"y","Y"]:
            help.helpcommand()
        command()