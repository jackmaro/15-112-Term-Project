from cmu_graphics import *
from otClasses import *
from otClassFns import*
from survivalHelpers import *
import math


def dayPass(app,travelOrNot):
    if travelOrNot:
        stamLoss = -1*rounded(getTruePace(app)*1.5)
        print(stamLoss)
        partyStatusChange(app,"stam",stamLoss)
        rollForBrokenPieces(app)

    foodConsumed = app.foodRations*len(app.playerParty)
    waterConsumed = len(app.playerParty)*2 #2 liters per day
    applyHumanFunctions(app,foodConsumed,waterConsumed)
    if len(app.puQueue) != 0:
        app.runningPopUps = True
    app.days+=1        


def applyHumanFunctions(app,foodConsumed,waterConsumed):
    applyHumanPartyFunctions(app,foodConsumed,waterConsumed)
    applyByPMFunctions(app)



def rollForBrokenPieces(app):
    thresh = 2
    if app.pace==15: thresh*=8
    elif app.pace==12: thresh*=4
    elif app.pace==9: thresh*=2
    rollRes = randrange(1,101)
    if rollRes<=thresh:
        possPieces = ["Wheels","Tongues","Axles"]
        pieceBroken = possPieces[randrange(0,3)]
        if app.player.inventory[pieceBroken]<=0:
            playerDeath(app,"broken wagon")
        else:
            app.puQueue.append(popUp(f'''One of the {pieceBroken} broke! You fix it.'''))
            app.player.alterInv(pieceBroken,-1)
        pass
