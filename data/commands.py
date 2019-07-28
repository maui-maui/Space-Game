#####################
### Basic Imports ###
#####################
import os
import time
import sys
######################
### Custom Imports ###
######################
from . import help
from . import definitions
######################

def playerchart(): # Player info
    pm = definitions.player.stats["money"]
    pp1 = definitions.player.stats["photons"]
    pp2 = definitions.player.stats["phasers"]
    pws = definitions.player.stats["warpspeed"]
    pc = definitions.player.stats["cannon"]
    pp = definitions.player.stats["probes"]
    lq = definitions.playerlocation.location["quadrant"]
    ls = definitions.playerlocation.location["sector"]
    lx = definitions.playerlocation.location["gridx"]
    ly = definitions.playerlocation.location["gridy"]
    hd = definitions.damage.damage["hull"]
    wdd = definitions.damage.damage["warpdrive"]
    sd = definitions.damage.damage["scanners"]
    td = definitions.damage.damage["transporter"]
    playerchart = (f"""
    <--- Status --->
Shields:
  -Front Shields: {definitions.fs}
  -Rear Shields: {definitions.bs}
  -Left Shields: {definitions.ls}
  -Right Shields: {definitions.rs}
Damage:
  -Hull: {hd}
  -Warp Drive: {wdd}
  -Scanners: {sd}
  -Trasporter: {td}
  -Shields: {definitions.avgshields}%
Player:
  -Money: {pm}
  -Photons: {pp1}
  -Phasers: {pp2}
  -Warp Speed: {pws}
  -Cannons: {pc}
  -Probes: {pp}
Location:
  -Quadrant: {lq}
  -Sector: {ls}
  -X Coord: {lx}
  -Y Coord: {ly}
Ship:
  -Ship Name: {definitions.status.status['shipname']}
MODE: ({definitions.player.stats["mode"]})
    """)
    print(playerchart)


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
########################################################################
################## Just Average out the shields ########################
########################################################################
def shieldsavg(fs,bs,ls,rs):
    avg = (fs + bs + ls + rs)/4
    return avg