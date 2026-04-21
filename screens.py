import cmu_graphics
from main import *

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
            #need to set up new game; perhaps should write helper for ts?
            #user = player(app.playerName,"N",2) #for now you will always start as a YA enby bc pronouns are exhausting
        if app.playerName=="Lauren" or app.playerName=="Kosbie":
            app.hardMode = True

    
#CODE FOR OCCUPATIONS SCREEN:
def playerOccupationScreen_redrawAll(app):
    professionsOptions = ["Banker", "Carpenter", "Farmer","Learn More"]
    drawOptions(app,professionsOptions)

def playerOccupationScreen_onKeyPress(app,key):
    professionsOptions = ["Banker", "Carpenter", "Farmer","Learn More"]
    learnKey="Professions"
    #fix ts later, lowk
    if chooseFromOptions(app,professionsOptions,learnKey,key)!=None and chooseFromOptions(app,professionsOptions,learnKey,key)!="learn":
        print("meow")    
    elif chooseFromOptions(app,professionsOptions,learnKey,key)==1:
        setActiveScreen("partyChoiceScreen")
        pass #ask Nick abt the issue here; would like to have one big "learn" thing with a huge dictionary for each like "learn" thing
    #
#functionList... hmm contemplate ts

def deathScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height, fill="lightGray")
    drawLabel(f"You have died of {app.deathReason}",app.width//2, app.height//2,fill="red",bold=True)

