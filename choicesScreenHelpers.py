from cmu_graphics import *
from otClassFns import *
from survivalHelpers import *


def shop(app):
    app.chosen="shop"
    setActiveScreen(shop)

def hunt(app):
    pass

#general menu functions
def travel(app):
    setActiveScreen("travelScreen")

def checkMap(app):
    #app.chosen="map"
    setActiveScreen("mapScreen")

def checkParty(app):
    #app.chosen="party"
    setActiveScreen("hpAndInvScreen")

def changePace(app):
    #app.chosen = "pace"
    paces = ["9 Miles/Day (Steady)","12 Miles/Day (Tiresome)","15 Miles/Day (Grueling)"]
    app.chosenFns = [[setPace,[app,9]],[setPace,[app,12]],[setPace,[app,15]]]
    app.chosenOptions = paces

def setPace(app,newPace):
    app.pace = newPace

def setFoodRation(app,newFood):
    app.foodRations = newFood

def changeFood(app):
    #app.chosen="food"
    foodRations = ["4 lbs/Day (Filling)", "2 lbs/Day (Meager)", "1 lb/Day (Grim)"]
    app.chosenOptions=foodRations
    app.chosenFns = [[setFoodRation,[app,4]],[setFoodRation,[app,2]],[setFoodRation,[app,1]]]

def rest(app):
    app.days+=1
    stamRegenRate = 24-getTruePace(app.pace)
    partyStatusChange(app,"stam",stamRegenRate)
    #dayPass(app)
    #app.milesTraveled-= math.floor(app.pace) #bc dayPass does this automatically

def partyStatusChange(app,hpOrStam,rateOfRegen):
    for folk in app.playerParty:
        folk.alterHPStam(hpOrStam,rateOfRegen)
        if (rateOfRegen<0) and (folk.checkDeath()!=None): #short circuits if gaining health
            applyDeath(app,folk,folk.checkDeath())

def applyDeath(app,folk,reason):
    pass
