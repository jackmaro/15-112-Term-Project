#general imports
from cmu_graphics import *
import string
import random

#importing from the individually organized files
from screens import *
from personAndPlayer import *
from conditions import *


def main():
    runAppWithScreens(initialScreen="gameStartScreen")
    
def onAppStart(app):
    app.playerName = ""
    app.playerParty = []
    app.godmode = False
    app.hardMode = False
    app.prevScreenChoices = None
    app.learnDict = {"Professions":"These are different professions you can choose from to get different effects on your point value stuff later!"}
    
def chooseFromOptions(app,optionsList,functionsList,key):
    if key.isalpha(): return None
    elif int(key) in range(1,len(optionsList)+1):
        newKey = int(key)-1
        print(functionsList[newKey][1])
        if type(functionsList[newKey][1])!=list:
            functionsList[newKey][0](app,functionsList[newKey][1])
        else:
            functionsList[newKey][0](app,*functionsList[newKey][1])

#DRAWING RELATED FUNCTIONS / VIEW FUNCTIONS
def partyChoiceScreen_onAppStart(app): #lowkey will move this at some point
    generateParty(app)
        

def drawOptions(app,optionsList):
    screenLength = app.height-app.height/6
    for i in range(len(optionsList)):
        yCoord = app.height/6 + i*screenLength/len(optionsList)
        drawLabel(f'{i+1}. {optionsList[i]}',10,yCoord,align='left',size=20) #magic number core teehee

def mapScreen_redrawAll(app):
    #probably import a pixelart drawn thing here
    #add a line over it showing where you've been'
    pass


#death screen
def playerDeath(app):
    pass

main()
