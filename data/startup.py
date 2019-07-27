######################
### Custom Imports ###
######################
from . import commands
from . import settings
######################

def start(): # The Start up of game
    print("""
*--------------------------------*
Welcome to Space Exploration Game
                   coded in Py3.7
     By: DrProfMaui
*--------------------------------*
""")
    settings.setname()
    settings.setshipname()
    commands.command()