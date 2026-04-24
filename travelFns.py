from cmu_graphics import *
from otClasses import *
from survivalHelpers import *
import math

#THIS IS WHAT I'M WORKING ON NOW
def dayPass(app):
    foodConsumed = app.foodRations*len(app.playerParty)
    waterConsumed = len(app.playerParty)*2 #2 liters per day
    app.milesTraveled+= math.floor(getTruePace(app)) 

    #feeding folks
    if app.player.inventory["Food"]<foodConsumed:
        app.player.inventory["Food"]=0
        #applyPartyDamage(app,5)
    else:
        app.player.alterInv("Food",-foodConsumed)
    #water stuff
    if app.player.inventory["Water"]<waterConsumed:
        litersNeeded = waterConsumed-app.player.inventory["Water"]
        app.player.inventory["Water"]=0
        rollForWaterDiseases(app,litersNeeded) 
        #ROLL FOR CHOLERA / DYSENTARY
    else:
        app.player.alterInv["Water",-waterConsumed]
    #roll for broken bones
    
    #ageUp
    if app.days%25==0:
        for pm in app.playerParty:
            pm.ageUp()
            if pm.health>getHPStamByAge(pm.age):
                pm.health=getHPStamByAge(pm.age)
    

    
    




def rollForWaterDiseases(app,litersNeeded):
    dysentaryThreshold = 2.5*litersNeeded
    choleraThreshold = 2*litersNeeded
    rollRes = randrange(1,101)
    if rollRes<=dysentaryThreshold:
        pass
    if rollRes<=choleraThreshold:
        pass

def rollForBrokenBones(app,folkIndex):
    thresh = 3
    folk = app.playerParty[folkIndex]
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
        bb =condition("Broken Bone","hp",1) #stage tbd
        folk.addCondition(bb)







    #need new temperature (if time)
