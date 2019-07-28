#####################
### Basic Imports ###
#####################

######################
### Custom Imports ###
######################
from . import help
from . import definitions
from utils import *
######################

def mapgen():
	map_generation.generate_sector(size = 15)
