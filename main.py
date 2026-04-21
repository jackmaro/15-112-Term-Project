#general imports
from cmu_graphics import *
import string
import random

#importing from the individually organized files
from personAndPlayer import *
from screens import *
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
    

#im mixed on where to put this.
def chooseFromOptions(app,optionsList,learnKey,key):
    if key.isalpha(): return None
    elif int(key) in range(len(optionsList)):
        return optionsList[int(key)-1]
    elif int(key)==len(optionsList):
        return app.learnDict[learnKey]
    else:
        return None

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
