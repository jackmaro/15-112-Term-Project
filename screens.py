from cmu_graphics import *
from main import *
from choicesFunctions import *
from learn import *
import string

#CODE FOR START SCREEN
def gameStartScreen_redrawAll(app):
    drawLabel("The Oregon Trail", app.width//2, app.height/8, bold=True,size=20)
    drawLabel("Press 's' to start!", app.width//2, app.height/4, bold=True)

def gameStartScreen_onKeyPress(app,key):
    if key=="s":
        setActiveScreen("playerNameScreen")

#CODE FOR PLAYER NAME SCREEN:
def playerNameScreen_redrawAll(app):
    drawLabel("Welcome to the Oregon Trail!! ADD DESCRIPTION STUFF LATER",app.width//2, app.height/8)
    drawLabel("But first...", app.width//2,app.height/5)
    drawLabel("What should we call you?", app.width//2, app.height/3, bold=True, size=16)
    if app.playerName=="":
        drawLabel("<Type your name here>",app.width//2,app.height/2)
    else:
        drawLabel(f'{app.playerName}',app.width//2,app.height/2)

def playerNameScreen_onKeyPress(app,key):
    if key=='backspace' and len(app.playerName)!=0:
        app.playerName = app.playerName[:-1]
    elif 0<=len(app.playerName)+len(key)<=8 and (key in string.ascii_letters): #NTS: figure out how to not have it input like backspace and such
        app.playerName+=str(key)
    elif key=='enter' and app.playerName!="":
        setActiveScreen("playerOccupationScreen")
        if app.playerName=="meow":
            app.godmode=True
            app.player = player(app.playerName,2)
        if app.playerName=="Lauren" or app.playerName=="Kosbie":
            app.hardMode = True
            app.player = player(app.playerName,4)
        else:
            app.player = player(app.playerName,2)

    
#CODE FOR OCCUPATIONS SCREEN:
def playerOccupationScreen_redrawAll(app):
    professionsOptions = ["Banker", "Carpenter", "Farmer","Learn More"]
    drawOptions(app,professionsOptions)

def playerOccupationScreen_onKeyPress(app,key):
    professionsOptions = ["Banker", "Carpenter", "Farmer","Learn More"]
    fnsList = [[applyProfession,"Banker"],[applyProfession,"Carpenter"],[applyProfession,"Farmer"],[learnMore,"professions"]]
    chooseFromOptions(app,professionsOptions,fnsList,key)
    
def deathScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height, fill="lightGray")
    drawLabel(f"You have died of {app.deathReason}",app.width//2, app.height//2,fill="red",bold=True)

