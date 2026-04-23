from cmu_graphics import *
from buttonClass import *
from optionsFns import *
from choicesFunctions import *
from learn import *
from personAndPlayer import *
import string

#CODE FOR START SCREEN
def ontoNameScreen(app):
    print("Meow")
    setActiveScreen("playerNameScreen")

def gameStartScreen_onScreenActivate(app):
    app.startButton = button(app.width//2,app.height//2+20,100,50,ontoNameScreen,"START!","blue")

def gameStartScreen_redrawAll(app):
    drawLabel("The Oregon Trail", app.width//2, app.height/8, bold=True,size=20)
    app.startButton.draw()
    drawLabel("Press 's' to start!", app.width//2, app.height/4, bold=True)

def gameStartScreen_onMousePress(app,mouseX,mouseY):
    if app.startButton.isIn(mouseX,mouseY):
        print("meow")
        setActiveScreen("playerNameScreen")
    #if app.startButton.isIn(mouseX,mouseY):
    #    app.startButton.runFn(app)

#perhaps refashion this below into a "skip" button
def gameStartScreen_onKeyPress(app, key):
    if key=="s":
        app.playerName="Meow"
        app.player = player(app.playerName,2)
        app.godmode=True
        app.playerParty = [app.player,person("Olivia",2),person("Jacob",3), person("JJ",3),person("JK",4)]
        app.player.alterInv("Oxen",8)
        app.player.alterInv("Wheels",4)
        app.player.alterInv("Tongues",3)
        app.player.alterInv("Axles",3)
        app.player.alterInv("Ammo",5000)
        app.player.alterInv("Food",5000)
        setActiveScreen("hpAndInvScreen") #can change as desired for debugging



#CODE FOR PLAYER NAME SCREEN:
def playerNameScreen_onScreenActivate(app):
    pass

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
def playerOccupationScreen_onScreenActivate(app):
    pass

def playerOccupationScreen_redrawAll(app):
    professionsOptions = ["Banker", "Carpenter", "Farmer","Learn More"]
    drawOptions(app,professionsOptions)

def playerOccupationScreen_onKeyPress(app,key):
    professionsOptions = ["Banker", "Carpenter", "Farmer","Learn More"]
    fnsList = [[applyProfession,"Banker"],[applyProfession,"Carpenter"],[applyProfession,"Farmer"],[learnMore,"professions"]]
    chooseFromOptions(app,professionsOptions,fnsList,key)
    
#CODE FOR PARTY NAME CHOICE SCREEN

#NEXT TO DO: WRITE THIS REDRAW ALL
def partyNamingScreen_onScreenActivate(app):
    generateParty(app)
    app.selectedPM = 1

def partyNamingScreen_redrawAll(app):
    partyNames = [app.player.name]+[item.name for item in app.playerParty]
    screenLength = app.height-app.height/6
    for i in range(len(partyNames)):
        yCoord = app.height/6 + i*screenLength/len(partyNames)
        color = "red" if i==app.selectedPM else "black"
        boldOrNot = True if i==0 else False
        if partyNames[i]!="":
            drawLabel(f'{i+1}. {partyNames[i]}',10,yCoord,align='left',size=20,fill=color,bold=boldOrNot) #magic number core teehee
        else:
            drawLabel(f'{i+1}. <Type Stuff Here!>',10,yCoord,align='left',size=20,fill=color, bold=boldOrNot) #partially for debugging, but also for 


def partyNamingScreen_onKeyPress(app,key):
    partyNames = [app.player.name]+[item.name for item in app.playerParty]
    print("" in partyNames)
    if key.isdigit():
        newKey = int(key)-1
        print(newKey)
        if newKey in range(1,len(partyNames)):
            app.selectedPM = newKey
    elif key in string.ascii_letters:
        if len(partyNames[app.selectedPM])<8:
            print(app.selectedPM)
            print(app.playerParty)
            currPM = app.playerParty[app.selectedPM-1]
            currPM.changeName(currPM.name+key)
    elif key=='backspace':
        currPM = app.playerParty[app.selectedPM-1]
        currPM.changeName(currPM.name[:-1])
    elif key=='down':
        if app.selectedPM<(len(partyNames)-1):
            app.selectedPM+=1
    elif key=='up':
        if app.selectedPM>1:
            app.selectedPM-=1
    elif key=='enter' and ("" not in partyNames):
        print("In here!")
        setActiveScreen("journeyStart")

#CODE FOR JOURNEY BEGIN SCREEN?
def journeyStart_onScreenActivate(app):
    pass

def journeyStart_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="black")
    drawLabel(f"And now, my good {app.playerName}, your journey begins...",app.width/2, app.height/2,fill="white")




#CODE FOR SHOP SCREEN

#CODE FOR SHOW INVENTORY?
def shopScreen_redrawAll(app):
    pass

#CODE FOR SHOW HEALTH AND SUCH
def hpAndInvScreen_onScreenActivate(app):
    pass

def hpAndInvScreen_redrawAll(app):
    drawRect(0,0,app.width, app.height//3,fill="gray")
    drawLabel("Current Party Health", app.width//2,20,size=16,bold=True)
    drawHPStamBars(app)
    drawInv(app)


def travelScreen_redrawAll(app):
    pass

#CODE FOR MAP SCREEN
def mapScreen_redrawAll(app):
    #probably import a pixelart drawn thing here
    #add a line over it showing where you've been'
    pass


#CODE FOR DEATH SCREEN
def deathScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height, fill="lightGray")
    drawLabel(f"You have died of {app.deathReason}",app.width//2, app.height//2,fill="red",bold=True)

