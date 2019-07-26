from . import commands

def settings():
        choice = input("""
        Player Settings:
        cn -- Character Name
        cs -- Ship Name

        Game Settings:
        wm -- WASD mode for controlling ship
        tm -- TEXT mode for controlling ship
        """)
        if choice in ["cn","name","NAME"]:
            commands.setname()
        elif choice in ["csn","cs","shipname","SHIPNAME"]:
            commands.setshipname()
