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
        
#party functions
    #party eats
    
    #roll for broken bones
def applyHumanPartyFunctions(app,foodConsumed,waterConsumed):
    if app.player.inventory["Food"]<foodConsumed:
        app.player.inventory["Food"]=0
        #apply party damage ahh fn (app,5)
    else:
        app.player.alterInv("Food",-foodConsumed)
    #party drinks
    if app.player.inventory["Water"]<waterConsumed:
        litersNeeded = waterConsumed-app.player.inventory["Water"]
        app.player.inventory["Water"]=0
        rollForWaterDiseases(app,litersNeeded) 
    else:
        app.player.alterInv["Water",-waterConsumed]
    #age up
    if app.days%25==0:
        for pm in app.playerParty:
            pm.ageUp()
            if pm.health>getHPStamByAge(pm.age):
                pm.health=getHPStamByAge(pm.age)


def applyByPMFunctions(app):
    for folk in app.playerParty:
        rollForBrokenBones(app, folk)
        




#DISEASES AND CONDITIONS AND SUCH    

def rollForWaterDiseases(litersNeeded): #this is applied randomly to someone in the party
    dysentaryThreshold = 2.5*litersNeeded
    choleraThreshold = 2*litersNeeded
    rollRes = randrange(1,101)
    if rollRes<=dysentaryThreshold:
        pass
    if rollRes<=choleraThreshold:
        pass

def rollForBrokenBones(app,folk): #this is by person
    thresh = 3
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
        bb =condition("Broken Bone","stam",1) #stage tbd
        folk.addCondition(bb)
