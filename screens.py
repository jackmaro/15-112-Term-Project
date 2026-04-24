from cmu_graphics import *
from buttonClass import *
from optionsFns import *
from choicesFunctions import *
from learn import *
from personAndPlayer import *
from travelFns import *
from travelScreenHelpers import *
import string

def returnToChoices(app):
    setActiveScreen("choices")

#CODE FOR START SCREEN
def ontoNameScreen(app):
    setActiveScreen("playerNameScreen")

def gameStartScreen_onScreenActivate(app):
    app.startButton = button(app.width//2,app.height//2+20,100,50,ontoNameScreen,"START!","blue")

def gameStartScreen_redrawAll(app):
    drawLabel("The Oregon Trail", app.width//2, app.height/8, bold=True,size=20)
    app.startButton.draw()
    drawLabel("Press 's' to start!", app.width//2, app.height/4, bold=True)

def gameStartScreen_onMousePress(app,mouseX,mouseY):
    if app.startButton.isIn(mouseX,mouseY):
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
        app.playerParty[3].alterHPStam("hp",-30)
        app.player.alterInv("Oxen",8)
        app.player.alterInv("Wheels",4)
        app.player.alterInv("Tongues",3)
        app.player.alterInv("Axles",3)
        app.player.alterInv("Ammo",5000)
        app.player.alterInv("Food",5000)
        setActiveScreen("travelScreen") #can change as desired for debugging



#CODE FOR PLAYER NAME SCREEN:
def playerNameScreen_onScreenActivate(app):
    pass

def playerNameScreen_redrawAll(app):
    drawLabel("Hello Traveler! Welcome to the Oregon Trail!",app.width//2, app.height/8)
    drawLabel("But first...", app.width//2,app.height/5)
    drawLabel("What should we call you?", app.width//2, app.height/3, bold=True, size=16)
    if app.playerName=="":
        drawLabel("<Type your name!>",app.width//2,app.height/2)
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
    fnsList = [[applyProfession,[app,"Banker"]],[applyProfession,[app,"Carpenter"]],[applyProfession,[app,"Farmer"]],[learnMore,[app,"professions"]]]
    chooseFromOptions(app,professionsOptions,fnsList,key)
    
#CODE FOR PARTY NAME CHOICE SCREEN

#NEXT TO DO: WRITE THIS REDRAW ALL
def partyNamingScreen_onScreenActivate(app):
    generateParty(app)
    app.selectedPM = 1

def partyNamingScreen_redrawAll(app):
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
        print("In here!")
        setActiveScreen("shop")

#CODE FOR SHOP SCREEN:
def shop_onScreenActivate(app):
    app.shopButtons = []

def shop_redrawAll(app):
    #nts: food is 20 cents per pound so we're doing 1 buck per 5 pounds; similarly water is 1 per 2 L, ammo is 2 per 20 ammos, 
    beginningPrices={'Oxen':30,'Wheels':10,'Tongues':10,'Axles':10, 'Ammo':2, 'Food':1,'Clothes':10,'Water':1}
    if app.milesTraveled==0:
        drawShop(app,"Jack's General Shop",beginningPrices)
    drawInv(app)

def shop_onKeyPress(app,key):
    if key=="right" and app.milesTraveled==0:
        setActiveScreen("journeyStart")


#CONTEMPLATE THE BUTTONS AND THIS ENTIRE MECHANIC LOWK
def drawShop(app,shopName,pricesDict):
    drawRect(0,0,app.width,app.height/3+20,fill="burlyWood") #approx 153
    drawLabel(f"{shopName}", app.width//2, 15,size=20,bold=True,align="bottom")
    drawLine(0,20,app.width,20,fill="black",lineWidth=1)
    itemsList = ["Oxen","Wheels","Tongues", "Axles","Food","Water","Clothes", "Ammo"]
    itemsMeasure = ["yoke","wheel","tongue","axle","pound","liter","set","20"]
    for i in range(len(itemsList)):
         row, col = i//4, i%4
         cellLX, cellTY = 50+85*col,30+60*row
         drawRect(cellLX,cellTY,80,50,fill=None,border="black")
         drawLabel(f'{itemsList[i]}',cellLX+5,cellTY+5,align="top-left",size=10)
         drawLabel(f'''${pricesDict[itemsList[i]]} per {itemsMeasure[i]}''',cellLX+5,cellTY+40,align="left",size=10)         

#CODE FOR JOURNEY BEGIN SCREEN?
def journeyStart_onScreenActivate(app):
    app.pace = 9 #miles/day; is the "steady" and does not drain stamina unless food bad ?
    app.foodRations = 3 #pounds/day, per person; water is 2 Liters/day per person
    app.days = 0 
    app.milesTraveled = 0
    def sJourneyButtonPress(app):
        setActiveScreen("choices")
    app.startJourneyButton = button(app.width/2,app.height/2+30,100,50,sJourneyButtonPress,"Press to begin your Travels!","blue")
    pass


def journeyStart_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="black")
    drawLabel(f"And now, my good {app.playerName}, your journey begins...",app.width/2, app.height/2,fill="white")
    app.startJourneyButton.draw()

def journeyStart_onMousePress(app,mouseX,mouseY):
    if app.startJourneyButton.isIn(mouseX,mouseY):
        app.startJourneyButton.runFn(app)


def choices_onScreenActivate(app):
    app.chosenOptions = None

def choices_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="lightGray")
    if app.milesTraveled==0:
        optionsList = ["Travel", "Check Map", "Check Party", "Change Pace", "Change Food Rations", "Rest", "Shop"]
    else:
        optionsList = ["Continue Traveling","Check Map", "Check Party", "Change Pace", "Change Food Rations","Rest", "Hunt"]
    if app.chosenOptions==None:
        drawOptions(app,optionsList)
    else:
        drawOptions(app,app.chosenOptions)

def choices_onKeyPress(app,key):
    print(key)
    if key=='escape':
        app.chosenOptions=None
    else:
        if app.chosenOptions==None:
            if app.milesTraveled==0:
                optionsList = ["Travel","Check Map", "Check Party", "Change Pace", "Change Food Rations","Rest", "Shop"]
                fnsList = [[travel,app],[checkMap,app],[checkParty,app],[changePace,app],[changeFood,app],[rest,app],[shop,app]]
            else:
                optionsList = ["Continue Traveling","Check Map","Check Party", "Change Pace", "Change Food Rations","Rest", "Hunt"]
                fnsList = [[travel,app],[checkMap,app],[checkParty,app],[changePace,app],[changeFood,app],[rest,app],[hunt,app]]
        if app.chosenOptions!=None:
            optionsList = app.chosenOptions
            fnsList = app.chosenFns
        chooseFromOptions(app,optionsList,fnsList,key)


def shop(app):
    app.chosen="shop"
    setActiveScreen(shop)

def hunt(app):
    pass

def partyStatusChange(app,hpOrStam,rateOfRegen):
    for folk in app.playerParty:
        folk.alterHPStam(hpOrStam,rateOfRegen)
        if (rateOfRegen<0) and (folk.checkDeath()!=None): #short circuits if gaining health
            applyDeath(app,folk,folk.checkDeath())

def applyDeath(app,folk,reason):
    pass


#CODE FOR SHOW HEALTH AND SUCH
def hpAndInvScreen_onScreenActivate(app):
    pass
def hpAndInvScreen_redrawAll(app):
    drawHPStamBars(app)
    drawInv(app)
def hpAndInvScreen_onKeyPress(app,key):
    if key=='escape':
        setActiveScreen("choices")


def travelScreen_redrawAll(app):
    drawTravelScreenTop(app)
    drawTravelScreenBottom(app)

def travelScreen_onScreenActivate(app):
    app.man = "cmu://1166311/46639916/mysteryMan.png"
    app.manX = 360
    app.landmarks = [landmark("Fort Hall",0),landmark("Fort Boise",rounded(app.milesOfTrail*0.4)),landmark("Blue Mountains",rounded(app.milesOfTrail*0.65)),landmark("The Dalles",rounded(app.milesOfTrail*0.8))]
    app.btmFromTravButton = button(75,360,115,35,returnToChoices,"Back to Options","burlyWood","saddleBrown",10)
    app.travDayButton = button(210,360,115,35,returnToChoices,"Travel a Day","burlyWood","saddleBrown",10)
    app.travelButtons = [app.btmFromTravButton,app.travDayButton]





#CODE FOR MAP SCREEN
def mapScreen_onScreenActivate(app):
    pass

def mapScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill="pink")
    #probably import a pixelart drawn thing here
    #add a line over it showing where you've been'
    pass

def mapScreen_onKeyPress(app,key):
    if key=='escape':
        app.chosen=None
        setActiveScreen("choices")



#CODE FOR DEATH SCREEN
def deathScreen_redrawAll(app):
    drawRect(0,0,app.width,app.height, fill="lightGray")
    drawLabel(f"You have died of {app.deathReason}",app.width//2, app.height//2,fill="red",bold=True)
    drawLabel(f'Press r to return to the start menu!', app.width//2, app.height//2+30, fill="black", bold=True)

def deathScreen_onKeyPress(app,key):
    if key=="r":
        setActiveScreen("gameStartScreen")
