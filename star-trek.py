import time
import os
import sys
import json
import random

from data.definitions import *
from data.classes import *
from data.commands import * 

with open('data/maps.json', 'r') as f:
    maps = json.load(f)

x = mapgen(planetarray)

mapsetting()

#print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in planetarray]))
startup()
