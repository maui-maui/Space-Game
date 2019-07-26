import random
import json
import time
from . import definitions
from . import classes
from . import help
from . import settings
import os
import sys

with open('data/maps.json', 'r') as f:
   maps = json.load(f)

def mapgen(planetarray):
    for row_index, row in enumerate(planetarray):
      for col_index, item in enumerate(row):
         if planetarray[row_index][col_index] != definitions.player:
            x = random.randint(1,10)
            if x <= 8:
               planetarray[row_index][col_index] = '#'
            elif x > 8:
               newRand = random.randint(1,10)
               if newRand <= 2:
                  planetarray[row_index][col_index] = 'P'
               elif newRand <= 4:
                  planetarray[row_index][col_index] = '*'
               elif newRand <= 6:
                  planetarray[row_index][col_index] = '^'
               elif newRand <= 8:
                  planetarray[row_index][col_index] = 'C'
               elif newRand == 9:
                  planetarray[row_index][col_index] = '!'
               else:
                  planetarray[row_index][col_index] = 'B'
            else:
               pass
    return

def mapsetting():
    for i in range(1,17):
        if i == 1:
            maps["sectoraa"] = definitions.planetarray

            with open('data/maps.json', 'w') as outfile:
             json.dump(maps, outfile)


def shieldsavg(fs,bs,ls,rs):
    avg = (fs + bs + ls + rs)/4
    return avg

def playerchart():
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
    """)
    print(playerchart)

def setname():
    name = input("What is your name captain?\n>>  ")
    print(f"Welcome aboard Captain {name}")

def setshipname():

    shipname = input("What shall we call your ship?\n>>  ")
    if len(shipname) <= 2:
        shnm = random.sample(["Deluxe","Voltage","Titan"],1)
        definitions.status.status["shipname"] = 'S.S.'.join(shnm)
    else:
        definitions.status.status["shipname"] = shipname
    print(f"Captain Your ship name is set to {definitions.status.status['shipname']}")
    command()

def movecommand():
    print("Move command:")
    time.sleep(1)
    def setquad():
        quadrant = input("Choose a quadrant(1-4): ")
        try:
            quadrant = int(quadrant)
            if quadrant <= 4:
                definitions.playerlocation.location["quadrant"] = quadrant
            else:
                print("Incorrect Value! Must be 1-4 only")
                setquad()
        except:
            print("Try Again! 1-4 only!")
            setquad()
    def setsector():
        sector = input("Choose a sector(1-4): ")
        try:
            sector = int(sector)
            if sector <= 4:
                definitions.playerlocation.location["sector"] = sector
            else:
                print("Incorrect Value! Must be 1-4 only")
                setsector()
        except:
            print("Try Again! 1-4 only!")
            setsector()
    def setgridy():
        gridy = input("Choose Your Y coordinate(1-9): ")
        try:
            gridy = int(gridy)
            if gridy <= 9:
                definitions.playerlocation.location["gridy"] = gridy
            else:
                print("Incorrect Value! Must be 1-9 only")
                setgridy()
        except:
            print("Try Again! 1-4 only!")
            setgridy()
    def setgridx():
        gridx = input("Choose your X coordinate(1-9): ")
        try:
            gridx = int(gridx)
            if gridx <= 9:
                definitions.playerlocation.location["gridx"] = gridx

            else:
                print("Incorrect Value! Must be 1-9 only")
                setgridx()
        except:
            print("Try Again! 1-4 only!")
            setgridx()
    def mvcmd():
        print(f"Current Quadrant: {definitions.playerlocation.location['quadrant']}")
        setquad()
        print(f"Current Quadrant now set to: {definitions.playerlocation.location['quadrant']}")
        time.sleep(1)
        print(f"Current Sector: {definitions.playerlocation.location['sector']}")
        setsector()
        print(f"Current Sector now set to: {definitions.playerlocation.location['sector']}")
        time.sleep(1)
        print(f"Current X: {definitions.playerlocation.location['gridx']}")
        setgridx()
        print(f"Current X now set to: {definitions.playerlocation.location['gridx']}")
        time.sleep(1)
        print(f"Current Y: {definitions.playerlocation.location['gridy']}")
        setgridy()
        print(f"Current Y now set to: {definitions.playerlocation.location['gridy']}")
        time.sleep(1)
        command()
    mvcmd()

def mapcommand():
    cquadrant = definitions.playerlocation.location["quadrant"]
    csector = definitions.playerlocation.location["sector"]
    cgridx = definitions.playerlocation.location["gridx"]
    cgridy = definitions.playerlocation.location["gridy"]
    print(f'LOCATION:\nQ: {cquadrant}\nS: {csector}\nG: {cgridy}-{cgridx}\n|\n|--> {cquadrant}-{csector}|{cgridy}-{cgridx}')
    print('')
    if cquadrant == 1:
        if csector == 1:
            print('\n'.join(list(' '.join(x) for x in maps['sectoraa'])))
            maps['sectoraa'][gridx][gridy] = '#'
            maps['sectoraa'][cgridx][cgridy] = '@'
        if csector == 2:
            print('\n'.join(list(' '.join(x) for x in maps['sectorab'])))
            maps['sectorab'][gridx][gridy] = '#'
            maps['sectorab'][cgridx][cgridy] = '@'
        if csector == 3:
            print('\n'.join(list(' '.join(x) for x in maps['sectorac'])))
            maps['sectorac'][gridx][gridy] = '#'
            maps['sectorac'][cgridx][cgridy] = '@'
        if csector == 4:
            print('\n'.join(list(' '.join(x) for x in maps['sectorad'])))
            maps['sectorad'][gridx][gridy] = '#'
            maps['sectorad'][cgridx][cgridy] = '@'
    if cquadrant == 2:
        if csector == 1:
            print('\n'.join(list(' '.join(x) for x in maps['sectorba'])))
            maps['sectorba'][gridx][gridy] = '#'
            maps['sectorba'][cgridx][cgridy] = '@'
        if csector == 2:
            print('\n'.join(list(' '.join(x) for x in maps['sectorbb'])))
            maps['sectorbb'][gridx][gridy] = '#'
            maps['sectorbb'][cgridx][cgridy] = '@'
        if csector == 3:
            print('\n'.join(list(' '.join(x) for x in maps['sectorbc'])))
            maps['sectorbc'][gridx][gridy] = '#'
            maps['sectorbc'][cgridx][cgridy] = '@'
        if csector == 4:
            print('\n'.join(list(' '.join(x) for x in maps['sectorbd'])))
            maps['sectorbd'][gridx][gridy] = '#'
            maps['sectorbd'][cgridx][cgridy] = '@'
    if cquadrant == 3:
        if csector == 1:
            print('\n'.join(list(' '.join(x) for x in maps['sectorca'])))
            maps['sectorca'][gridx][gridy] = '#'
            maps['sectorca'][cgridx][cgridy] = '@'
        if csector == 2:
            print('\n'.join(list(' '.join(x) for x in maps['sectorcb'])))
            maps['sectorcb'][gridx][gridy] = '#'
            maps['sectorcb'][cgridx][cgridy] = '@'
        if csector == 3:
            print('\n'.join(list(' '.join(x) for x in maps['sectorcc'])))
            maps['sectorcc'][gridx][gridy] = '#'
            maps['sectorcc'][cgridx][cgridy] = '@'
        if csector == 4:
            print('\n'.join(list(' '.join(x) for x in maps['sectorcd'])))
            maps['sectorcd'][gridx][gridy] = '#'
            maps['sectorcd'][cgridx][cgridy] = '@'
    if cquadrant == 4:
        if csector == 1:
            print('\n'.join(list(' '.join(x) for x in maps['sectorda'])))
            maps['sectorda'][gridx][gridy] = '#'
            maps['sectorda'][cgridx][cgridy] = '@'
        if csector == 2:
            print('\n'.join(list(' '.join(x) for x in maps['sectordb'])))
            maps['sectordb'][gridx][gridy] = '#'
            maps['sectordb'][cgridx][cgridy] = '@'
        if csector == 3:
            print('\n'.join(list(' '.join(x) for x in maps['sectordc'])))
            maps['sectordc'][gridx][gridy] = '#'
            maps['sectordc'][cgridx][cgridy] = '@'
        if csector == 4:
            print('\n'.join(list(' '.join(x) for x in maps['sectordd'])))
            maps['sectordd'][gridx][gridy] = '#'
            maps['sectordd'][cgridx][cgridy] = '@'

def warpcommand():
    print(f"Your current warp speed is {definitions.player.stats['warpspeed']}")
    choice = input("Would you like to change your warp speed? (Y/N)\n>> ")
    if choice in ["y","YES","Y","yes"]:
        setwarpspeed = int(input("Choose a speed between 1-10\n>> "))
        if setwarpspeed <= 10:
            definitions.player.stats["warpspeed"] = setwarpspeed
            print(f"Warp speed now set to: {definitions.player.stats['warpspeed']}")
            command()
        else:
            print("Incorrect Value! Try Again!")
            time.sleep(2)
            warpcommand()
    else:
        command()

def command():
    commands = input("COMMAND >> ")
    if commands in ["help","?"]:
        help.helpcommand()
    elif commands in ["? map","help map"]:
        help.helpmap()
    elif commands in ["? move","help move"]:
        help.helpmove()

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

def startup():
    print("""
--------------------------------
Welcome to Space Exploration Game
                   coded in py
     By: DrProfMaui
--------------------------------
""")
    setname()
    setshipname()
    command()

def shipchooser():
    print(f"Your ship is currently set to {shipname}")
