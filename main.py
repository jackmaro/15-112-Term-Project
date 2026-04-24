#general imports
from cmu_graphics import *

#importing from the individually organized files
from screens import *
from personAndPlayer import *
from conditions import *


def main():
    runAppWithScreens(initialScreen="gameStartScreen")
    
def onAppStart(app):
    app.width=400
    app.height=400
    app.milesTraveled = 0
    app.days = 0
    app.milesOfTrail = 450
    app.playerName = ""
    app.playerParty = []
    app.godmode = False
    app.hardMode = False
    app.prevScreenChoices = None
    app.learnDict = {"Professions":"These are different professions you can choose from to get different effects on your point value stuff later!"}
    

main()
