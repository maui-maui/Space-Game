

class Character:
    def __init__(self, money, photons, phasers, cannon, warpspeed, probes):
        self.stats = {
            "money" : money,
            "photons" : photons,
            "phasers" : phasers,
            "cannon" : cannon,
            "warpspeed" : warpspeed,
            "probes" : probes
        }
class Location:
    def __init__(self, quadrant, sector, gridx, gridy):
        self.location = {
            "quadrant" : quadrant,
            "sector" : sector,
            "gridx" : gridx,
            "gridy" : gridy
        }

class Damage:
    def __init__(self,hull,shields,warpdrive,scanners,transporter):
        self.damage = {
            "hull" : hull,
            "shields" : shields,
            "warpdrive" : warpdrive,
            "scanners" : scanners,
            "transporter" : transporter
        }
class Shields:
    def __init__(self,front,rear,left,right,power,energy):
        self.shields = {
            "front":front,
            "right":right,
            "left":left,
            "rear":rear,
            "power":power, #different for each ship hit points it can block
            "energy":energy, #different for each ship how much energy it can hold takes x amt per y time
        }

class Ship:
    def __init__(self,shipname,shieldsstatus,energy,totalenergy,warptime):
        self.status = {
            "shipname":shipname,
            "shieldsstatus":shieldsstatus,
            "energy":energy,
            "totalenergy":totalenergy,
            "warptime":warptime #time it takes to move one square
        }