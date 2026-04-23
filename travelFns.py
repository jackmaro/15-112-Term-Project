from buttonClass import *
from personAndPlayer import *
from conditions import *
import math

#either that or let stamina loss be dictated by ts
def getTruePace(app):
    return (app.player.inventory["Oxen"]/4)*app.pace

def ageFolksUp(app):
    for folk in app.playerParty:
        folk.ageUp()

def checkForDeath(app):
    checkHPStam(app)
    pass
    
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
        

#THIS IS WHAT I'M WORKING ON NOW
def dayPass(app):
    foodConsumed = app.foodRations*len(app.playerParty)
    app.milesTraveled+= math.floor(getTruePace(app))
    if app.player.inventory["Food"]<foodConsumed:
        app.player.inventory["Food"]=0
        #applyPartyDamage(app,5)
    else:
        app.player.alterInv("Food",-foodConsumed)
