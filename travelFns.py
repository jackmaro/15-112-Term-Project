from cmu_graphics import *
from otClasses import *
from otClassFns import*
from survivalHelpers import *
import math


def dayPass(app,travelOrNot):
    if travelOrNot:
        stamLoss = rounded(getTruePace(app)*0.5)
        partyStatusChange(app,"stam",-stamLoss)
        rollForBrokenPieces(app)

    foodConsumed = app.foodRations*len(app.playerParty)
    waterConsumed = len(app.playerParty)*2 #2 liters per day
    applyHumanFunctions(app,foodConsumed,waterConsumed)
    app.days+=1

    
def applyHumanFunctions(app,foodConsumed,waterConsumed):
    applyHumanPartyFunctions(app,foodConsumed,waterConsumed)
    applyByPMFunctions(app)



def rollForBrokenPieces(app):
    thresh = 3.5
    if app.pace==15: thresh*=8
    elif app.pace==12: thresh*=4
    elif app.pace==9: thresh*=2
    rollRes = randrange(1,101)
    if rollRes<=thresh:
        #pseudo code: break a piece. if in inventory, prob solved. if not, game over w
        #death by no wagon
        pass

