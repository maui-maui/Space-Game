######################
### Custom Imports ###
######################
from data.settings import *
from data.commands import * 
######################

def start():
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