from cmu_graphics import *
from screens import *

def main():
    runAppWithScreens(initialScreen="gameStartScreen")
    
def onAppStart(app):
    app.width=400
    app.height=400
    app.milesTraveled = 0
    app.days = 0
    app.milesOfTrail = 220 #for brevity
    app.atLM=False
    app.playerName = ""
    app.playerParty = []
    app.godmode = False
    app.hardMode = False
    

main()
