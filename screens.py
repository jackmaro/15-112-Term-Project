from cmu_graphics import *
from optionsFns import *
from travelFns import *
from travelScreenHelpers import *
import string




def returnToChoices(app):
    setActiveScreen("choices")

#========================================================
#FULL GAME START SCREEN
#========================================================
def gameStartScreen_onScreenActivate(app):
    app.startButton = button(app.width//2-50,app.height//2+20,100,50,setActiveScreen,"playerNameScreen","START","skyBlue")

def gameStartScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="wheat")
    drawLabel("The Oregon Trail", app.width//2, app.height//4+50, bold=True,size=42.5)
    app.startButton.draw()

def gameStartScreen_onMousePress(app,mouseX,mouseY):
    if app.startButton.isIn(mouseX,mouseY):
        setActiveScreen("playerNameScreen")

#the so called god-mode function (s to skip)
def gameStartScreen_onKeyPress(app, key):
    if key=="s":
        app.playerName="Meow"
        app.player = player(app.playerName,2)
        app.godmode=True
        app.milesTraveled = 10
        app.atLM=False
        app.foodRations = 3
        app.pace=9
        app.playerParty = [app.player,person("Olivia",2),person("Jacob",3), person("JJ",3),person("JK",4)]
        app.playerParty[3].alterHPStam("hp",-100)
        app.player.alterInv("Oxen",8)
        app.player.alterInv("Wheels",4)
        app.player.alterInv("Tongues",3)
        app.player.alterInv("Axles",3)
        app.player.alterInv("Food",300)
        app.player.alterInv("Water",300)
        setActiveScreen("travelScreen") #can change as desired for debugging
#helper for button
def ontoNameScreen(app):
    setActiveScreen("playerNameScreen")


#========================================================
#PLAYER NAME SCREEN
#========================================================
def playerNameScreen_onScreenActivate(app):
    pass

def playerNameScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="lightGray")
    drawLabel("Hello Traveler,",app.width//2, app.height/8,size=15)
    drawLabel("Today you embark on a gruesome journey",app.width//2,app.height/8+25,size=15)
    drawLabel("from Fort Hall, Wyoming to Oregon City,Oregon.", app.width//2,app.height/8+50,size=15)
    drawLabel("Say, what's your name?", app.width//2, app.height/8+75, bold=True, size=15)
    if app.playerName=="":
        drawLabel("<Type your name!>",app.width//2,app.height/2,size=20)
    else:
        drawLabel(f'{app.playerName}',app.width//2,app.height/2,size=20)
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

#========================================================
#PLAYER OCCUPATION SCREEN
#========================================================
def playerOccupationScreen_onScreenActivate(app):
    pass
def playerOccupationScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="lightGray")
    drawLabel(f''' "{app.playerName}"? Well alright. I've no doubt you've led''',app.width//2,5,align="top",size=15)
    drawLabel("an interesting life with a name like that. So then,",app.width//2,20,align="top",size=15)
    drawLabel('''who were you before you set off on this journey?''',app.width//2,35,align="top",size=15,bold=True)
    drawLabel('''<Press the corresponding option's number!>''',app.width//2,350,size=15)
    professionsOptions = ["Banker", "Carpenter", "Farmer"]
    drawOptions(app,professionsOptions)
def playerOccupationScreen_onKeyPress(app,key):
    professionsOptions = ["Banker", "Carpenter", "Farmer"]
    fnsList = [[applyProfession,[app,"Banker"]],[applyProfession,[app,"Carpenter"]],[applyProfession,[app,"Farmer"]]]
    chooseFromOptions(app,professionsOptions,fnsList,key)
    
#========================================================
#PARTY NAMING SCREEN
#========================================================
def partyNamingScreen_onScreenActivate(app):
    generateParty(app)
    app.selectedPM = 1
def partyNamingScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="lightGray")
    drawLabel(f'''I see you have friends with you.''',app.width//2,5,align="top",size=15)
    drawLabel("Who are they?",app.width//2,25,align="top",size=15)
    drawLabel("<Use the up/down arrows or numbers to change friend!>",app.width//2,app.height-25,size=15)
    partyNames = [item.name for item in app.playerParty]
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
    partyNames = [item.name for item in app.playerParty]
    if key.isdigit():
        newKey = int(key)-1
        if newKey in range(1,len(partyNames)):
            app.selectedPM = newKey
    elif key in string.ascii_letters:
        if len(partyNames[app.selectedPM])<8:
            currPM = app.playerParty[app.selectedPM]
            currPM.changeName(currPM.name+key)
    elif key=='backspace':
        currPM = app.playerParty[app.selectedPM]
        currPM.changeName(currPM.name[:-1])
    elif key=='down':
        if app.selectedPM<(len(partyNames)-1):
            app.selectedPM+=1
    elif key=='up':
        if app.selectedPM>1:
            app.selectedPM-=1
    elif key=='enter' and ("" not in partyNames):
        setActiveScreen("shop")

#========================================================
#SHOP SCREEN
#========================================================
from shopScreenHelpers import *

def shop_onScreenActivate(app):
    beginningPrices = {'Oxen':30,'Wheels':10,'Tongues':10,'Axles':10, 'Food':1,'Water':1}
    if app.milesTraveled==0:
        app.currPriceDict = beginningPrices
    else:
        app.currPriceDict = generatePriceDict(beginningPrices)
    app.currStoreButtons = generateStoreButtons(app)
def shop_redrawAll(app):
    if app.milesTraveled==0:
        drawShop(app,"Jack's General Shop")
        if app.journeyStarted==False:
            drawLabel("Take some of my wares for your journey.",app.width//2,350,size=15,align="top")
            drawLabel("<Press the right arrow key to continue!>",app.width//2,375,size=15,align="top")
        if app.journeyStarted==True:
            drawLabel("<Press 'escape' to return to the menu!>",app.width//2,375,size=15,align="top")
    else:
        drawShop(app, "General Shop")
    drawInv(app)
def shop_onKeyPress(app,key):
    if key=="right" and app.milesTraveled==0 and app.journeyStarted==False:
        setActiveScreen("journeyStart")
    if key=="escape" and app.journeyStarted==True:
        setActiveScreen("choices")
def shop_onMousePress(app,mouseX,mouseY):
    for butt in app.currStoreButtons:
        if butt.isIn(mouseX,mouseY):
            butt.runFn()


#========================================================
#JOURNEY START SCREEN
#========================================================
def journeyStart_onScreenActivate(app):
    app.journeyStarted=True
    app.pace = 9 #miles/day; is the "steady" and does not drain stamina
    app.foodRations = 3 #pounds/day, per person; water is 2 Liters/day per person
    app.days = 0 
    app.milesTraveled = 0
    app.startJourneyButton = button(app.width/2-50,app.height/2-20,100,50,setActiveScreen,"choices","Begin","blue")

def journeyStart_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="black")
    drawLabel(f"And now, young {app.playerName}...",app.width/2, app.height/2-70,fill="white",size=20)
    drawLabel("...your journey begins...", app.width/2, app.height/2-50,fill="white",size=20)
    app.startJourneyButton.draw()

def journeyStart_onMousePress(app,mouseX,mouseY):
    if app.startJourneyButton.isIn(mouseX,mouseY):
        app.startJourneyButton.runFn()


#========================================================
#CHOICES SCREEN
#========================================================
from choicesScreenHelpers import *

def choices_onScreenActivate(app):
    app.chosenOptions = None

def choices_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="lightGray")
    drawLabel("Menu",app.width//2,25,size=20,bold=True)
    drawLine(0,50,app.width,50,fill="black")
    if app.milesTraveled==0 or (app.atLM==True):
        optionsList = ["Travel", "Check Map", "Check Party", "Change Pace", "Change Food Rations", "Rest", "Shop"]
    else:
        optionsList = ["Continue Traveling","Check Map", "Check Party", "Change Pace", "Change Food Rations","Rest"]
    if app.chosenOptions==None:
        drawOptions(app,optionsList)
    else:
        drawOptions(app,app.chosenOptions)

def choices_onKeyPress(app,key):
    if key=='escape':
        app.chosenOptions=None
    else:
        if app.chosenOptions==None:
            if app.milesTraveled==0:
                optionsList = ["Travel","Check Map", "Check Party", "Change Pace", "Change Food Rations","Rest", "Shop"]
                fnsList = [[travel,app],[checkMap,app],[checkParty,app],[changePace,app],[changeFood,app],[rest,app],[shop,app]]
            else:
                optionsList = ["Continue Traveling","Check Map","Check Party", "Change Pace", "Change Food Rations","Rest"]
                fnsList = [[travel,app],[checkMap,app],[checkParty,app],[changePace,app],[changeFood,app],[rest,app]]
        if app.chosenOptions!=None:
            optionsList = app.chosenOptions
            fnsList = app.chosenFns
        chooseFromOptions(app,optionsList,fnsList,key)


#========================================================
#HP AND INVENTORY SCREEN
#========================================================
from hpScreenHelpers import *
from invScreenHelpers import *
def hpAndInvScreen_onScreenActivate(app):
    pass
def hpAndInvScreen_redrawAll(app):
    drawHPStamBars(app)
    drawInv(app)
def hpAndInvScreen_onKeyPress(app,key):
    if key=='escape':
        setActiveScreen("choices")

#========================================================
#TRAVEL SCREEN
#========================================================
from travelScreenHelpers import *

def travelScreen_redrawAll(app):
    drawTravelScreenTop(app)
    drawTravelScreenBottom(app)
    if app.runningPopUps and len(app.puQueue)!=0:
        app.puQueue[0].draw()
    

def travelScreen_onScreenActivate(app):
    app.runningPopUps = False
    app.landmarks = [landmark("Fort Hall",0),landmark("Fort Boise",rounded(app.milesOfTrail*0.4)),landmark("Blue Mountains",rounded(app.milesOfTrail*0.65)),landmark("The Dalles",rounded(app.milesOfTrail*0.8))]
    app.btmFromTravButton = button(75,360,115,35,setActiveScreen,"choices","Back to Options","burlyWood","saddleBrown",10)
    app.travDayButton = button(210,360,115,35,travButton,app,"Travel a Day","burlyWood","saddleBrown",10)
    app.travelButtons = [app.btmFromTravButton,app.travDayButton]

def travelScreen_onMousePress(app,mouseX,mouseY):
    for butt in app.travelButtons:
        if butt.isIn(mouseX,mouseY):
            butt.runFn()
def travelScreen_onKeyPress(app,key):
    if app.runningPopUps and key=='space':
        app.puQueue.pop(0)



#========================================================
#MAP SCREEN
#========================================================
def mapScreen_onScreenActivate(app):
    pass
def mapScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="pink")
    #probably import a pixelart drawn thing here
def mapScreen_onKeyPress(app,key):
    if key=='escape':
        app.chosen=None
        setActiveScreen("choices")



#========================================================
#DEATH SCREEN
#========================================================
def deathScreen_onScreenActivate(app):
    app.dsButton = button(app.width//2-50,app.height//2,100,50,setActiveScreen,"gameStartScreen","Try Again","white","black")

def deathScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height, fill="gray")
    drawLabel(f"You have died of {app.deathReason}",app.width//2, app.height//2-40,fill="red",bold=True)
    app.dsButton.draw()

def deathScreen_onMousePress(app,mouseX,mouseY):
    if app.dsButton.isIn(mouseX,mouseY):
        app.dsButton.runFn()
