from cmu_graphics import *
from otClassFns import *
from survivalHelpers import *
from travelFns import *


def shop(app):
    setActiveScreen("shop")

#general menu functions
def travel(app):
    setActiveScreen("travelScreen")

def checkMap(app):
    setActiveScreen("mapScreen")

def checkParty(app):
    setActiveScreen("hpAndInvScreen")

def changePace(app):
    paces = ["9 Miles/Day (Steady)","12 Miles/Day (Tiresome)","15 Miles/Day (Grueling)"]
    app.chosenFns = [[setPace,[app,9]],[setPace,[app,12]],[setPace,[app,15]]]
    app.chosenOptions = paces

def setPace(app,newPace):
    app.pace = newPace

def setFoodRation(app,newFood):
    app.foodRations = newFood

def changeFood(app):
    foodRations = ["4 lbs/Day (Filling)", "2 lbs/Day (Meager)", "1 lb/Day (Grim)"]
    app.chosenOptions=foodRations
    app.chosenFns = [[setFoodRation,[app,4]],[setFoodRation,[app,2]],[setFoodRation,[app,1]]]

def rest(app):
    stamRegenRate = max(30-getTruePace(app),10)
    partyStatusChange(app,"stam",stamRegenRate)
    dayPass(app,False)