import random
import json
import time
from . import definitions
from . import commands
from . import classes
import os
import sys

with open('data/maps.json', 'r') as f:
   maps = json.load(f)

def helpcommand():
    print("""
This is the help menu...
    You can access this menu at anytime by typing 'help' or '?'
    (without the quotes) when your prompted for a command.

    To get help on a specific command type either ? command or
    'help command'(without the quotes).

    *move - Move around the map.
    warp - Set your warp speed (1-10).
    transport - If your in orbit of a planet or docked at a base you can transport to either the planet or the base.
    dock - Dock into a base if you are on one of the adjacent places.
    orbit - Orbit a planet.
    status - Info
    damage -
    logs -
    missions -
    repairs -
    warp - Change your warp speed.
    planet scanner -
    mine -
    search -
    chart -
    srscan - Scans the current quadrant(Sectors 1-4 of quadrant x).
    lrscan - Scans all 4 quadrants.
    scan -
    *map - Current Maps.
    sector chart -
    probe -

    quit - Quit Game
    clear - Clear screen
    settings - Change your settings
    """)
    commands.command()

def helpmap2():
        print("""
LOCATION ranges:
Quadrant: 1-4
Sector: 1-4
Grid: y = 1-9 x = 1-9
LOCATION Example:
Q: 1
S: 2
G: 6-2
|
|--> 1-2|6-2
    """)

def helpmap():
    print(f"{definitions.mapkey}")
    time.sleep(2)
    print(f"{definitions.mapquads}")
    time.sleep(2)
    print(f"{definitions.mapsectors}")
    time.sleep(2)
    print(f"{definitions.fullmap}")
    time.sleep(2)
    helpmap2()
    commands.command()

def helpmove():
    pass
