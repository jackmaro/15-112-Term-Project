from cmu_graphics import *
from otClasses import *
from otClassFns import *


def getTruePace(app):
    return max(rounded(app.player.inventory["Oxen"]/6)*app.pace,1)

def ageFolksUp(app):
    for folk in app.playerParty:
        folk.ageUp()

def applyHumanPartyFunctions(app,foodConsumed,waterConsumed):
    if app.player.inventory["Food"]<foodConsumed:
        foodDiff = foodConsumed-app.player.inventory["Food"]
        hpLoss = -1*rounded(0.5*foodDiff)
        app.player.inventory["Food"]=0
        partyStatusChange(app,"hp",hpLoss)
    else:
        hpGain = app.foodRations*4
        partyStatusChange(app,"hp",hpGain)
        app.player.alterInv("Food",-foodConsumed)
    if app.player.inventory["Water"]<waterConsumed:
        litersNeeded = waterConsumed-app.player.inventory["Water"]
        app.player.inventory["Water"]=0
        rollForWaterDiseases(app,litersNeeded) 
    else:
        app.player.alterInv("Water",-waterConsumed)
    #age up
    if app.days%25==0 and app.days!=0:
        app.puQueue.append(popUp("Happy Birthday! (Your party aged up)"))
        for pm in app.playerParty:
            pm.ageUp()
            if pm.health>getHPStamByAge(pm.age):
                pm.health=getHPStamByAge(pm.age)


def applyByPMFunctions(app):
    for folk in app.playerParty:
        rollForBrokenBones(app, folk)
        



#DISEASES!!! :D  
def rollForWaterDiseases(app, litersNeeded): #this is applied randomly to someone in the party
    dysentaryThreshold = 2.5*litersNeeded
    choleraThreshold = 2*litersNeeded
    rollRes = randrange(1,101)
    if rollRes<=dysentaryThreshold:
        app.puQueue.append(popUp("Your party has dysentery. Wuh-Oh."))
        partyStatusChange(app,"hp",-125,"dysentery")
    if rollRes<=choleraThreshold:
        app.puQueue.append(popUp("Your party has cholera."))
        partyStatusChange(app,"hp",-100,"cholera")


def rollForBrokenBones(app,folk): #this is by person
    thresh = 1
    #modifier change from pace!
    if app.pace==15: thresh *= 2
    elif app.pace==12: thresh *= 1.5
    elif app.pace==9: thresh *= 1
    #modifier from age
    if folk.age==0: thresh*=3
    elif folk.age==3: thresh*=2
    elif 1<=folk.age<=2: thresh*=1.5
    elif folk.age==4: thresh*=4
    rollRes = randrange(1,101)
    if rollRes<=thresh:
        app.puQueue.append(popUp(f"{folk} has a broken bone!"))
        randrange(1,4)
        hpLoss = -0.1*randrange(1,4)*folk.health
        folk.alterHPStam("hp",hpLoss)
