from . import classes
from . import commands
from . import help
from . import settings
import random

mapkey = ("""
# Key:
# * = Stars
# P = Planets
# C = Enemy Commander
# ! = Enemy Base
# ^ = Enemy Ship
# B = Friendly Base
# @ = Your Location
""")

planetarray = [[0 for i in range(9)] for j in range(9)]
player = '@'
planetarray[4][4] = player

mapsectors = ("""
Example Sector Layout:
-----------------------
| | 1 2 3 4 5 6 7 8 9 |
-----------------------
|1| # # # # # # # # # |
|2| # B # # # # # # # |
|3| # # # # P # # # # |
|4| # # # # # # # # # |
|5| # # # # * # # # P |
|6| # C E # # # @ # # |
|7| # ! # # # # # # # |
|8| # * # # # # # # # |
|9| # # # # # # # P # |
-----------------------
""")
mapquads = ("""
Quadrants Layout:
-----------|------------
|          |           |
|    Q:    |     Q:    |
|   ONE    |    TWO    |
|          |           |
|          |           |
-----------|------------
|          |           |
|     Q:   |      Q:   |
|  THREE   |    FOUR   |
|          |           |
|          |           |
-----------|------------
""")

fullmap = ("""
Q1:            Q2:
|----|-----|   |-----|-----|
|S:  |S:   |   |S:   |S:   |
| 1  |  2  |   | 1   | 2   |
|----|-----|   |-----|-----|
|S:  |S:   |   |S:   |S:   |
| 3  | 4   |   | 3   | 4   |
|----|-----|   |-----|-----|
Q3:            Q4:
|----|-----|   |-----|-----|
|S:  |S:   |   |S:   |S:   |
| 1  |  2  |   | 1   | 2   |
|----|-----|   |-----|-----|
|S:  |S:   |   |S:   |S:   |
| 3  | 4   |   | 3   | 4   |
|----|-----|   |-----|-----|
""")

shields = classes.Shields(100,100,100,20,100,2000)
fs = shields.shields["front"]
bs = shields.shields['rear']
ls = shields.shields['left']
rs = shields.shields["right"]

avgshields = commands.shieldsavg(fs,bs,ls,rs)

player = classes.Character("WASD",2000, 25, 25, 1000, 6, 5)
playerlocation = classes.Location(1,1,1,1)
damage = classes.Damage(0,avgshields,0,0,0)

status = classes.Ship(" ","on",2000,2000,1)
sn = status.status["shipname"]
ss = status.status["shieldsstatus"]
se = status.status["energy"]
ste = status.status["totalenergy"]
wt = status.status["warptime"]
