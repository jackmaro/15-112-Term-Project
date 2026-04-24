from cmu_graphics import *
from otClasses import *


def getTruePace(app):
    return (app.player.inventory["Oxen"]/4)*app.pace

def ageFolksUp(app):
    for folk in app.playerParty:
        folk.ageUp()

def checkForDeath(app):
    checkHPStam(app)
    pass
    
#revisit bc this is unneccessary
def checkHPStam(app):
    died = []
    for folk in app.playerParty:
        if folk.health<=0:
            died.append(folk)
            partyDeath(folk,"no health")
        elif folk.stam<=0:
            died.append(folk)
            partyDeath(folk,"exhaustion")
    return died

def partyDeath(folk,reason):
    print(f"{folk.name} has died of {reason}.")
    folk.status="dead"
        
