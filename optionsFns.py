from cmu_graphics import *
from personAndPlayer import *
from survivalHelpers import *
import math

def drawOptions(app,optionsList):
    screenLength = app.height-app.height/6
    for i in range(len(optionsList)):
        yCoord = app.height/6 + i*screenLength/len(optionsList)
        if optionsList[i]!="":
            drawLabel(f'{i+1}. {optionsList[i]}',10,yCoord,align='left',size=20) #magic number core teehee
        else:
            drawLabel(f'{i+1}. <Type Stuff Here!>',10,yCoord,align='left',size=20) #partially for debugging, but also for 


def chooseFromOptions(app,optionsList,functionsList,key):
    #option 1: choose using number inputs
    if key.isalpha(): return None
    elif int(key) in range(0,len(optionsList)+1):
        newKey = int(key)-1
        if type(functionsList[newKey][1])!=list:
            return functionsList[newKey][0](functionsList[newKey][1])
        else:
            return functionsList[newKey][0](*functionsList[newKey][1])
    #option 2: use arrows and enter??

#general menu functions
def travel(app):
    setActiveScreen("travelScreen")


def checkMap(app):
    #app.chosen="map"
    setActiveScreen("mapScreen")

def checkParty(app):
    #app.chosen="party"
    setActiveScreen("hpAndInvScreen")

def changeSmth(app,thing,value):
    app.thing = value

def changePace(app):
    #app.chosen = "pace"
    paces = ["9 Miles/Day (Steady)","12 Miles/Day (Tiresome)","15 Miles/Day (Grueling)"]
    app.chosenFns = [[setPace,[app,9]],[setPace,[app,12]],[setPace,[app,15]]]
    app.chosenOptions = paces

def setPace(app,newPace):
    app.pace = newPace
    print(app.pace)
def setFoodRation(app,newFood):
    app.foodRations = newFood

def changeFood(app):
    #app.chosen="food"
    foodRations = ["4 lbs/Day (Filling)", "2 lbs/Day (Meager)", "1 lb/Day (Grim)"]
    app.chosenOptions=foodRations
    app.chosenFns = [[setFoodRation,[app,4]],[setFoodRation,[app,2]],[setFoodRation,[app,1]]]

def rest(app):
    #app.chosen = "rest"
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
