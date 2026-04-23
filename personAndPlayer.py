# import random
# from main import *
from cmu_graphics import *

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age #for age, 0=child,1=teenager, 2=young adult, 3=adult, 4=old folk; has hp ramifications
        self.health = getHPStamByAge(self.age)
        self.happiness = 100
        self.stamina = getHPStamByAge(self.age)
        self.conditions = []
        self.status = "alive"

    def alterHPStam(self,hpVsStam,hpStamChange):
        if hpVsStam=="hp":
            self.health+=hpStamChange
            self.health%=getHPStamByAge(self.age)
        elif hpVsStam=="stam":
            self.stamina+=hpStamChange
            self.stamina%=getHPStamByAge(self.age)

    def addCondition(self,condt):
        self.conditions.append(condt)
    
    def removeCondition(self,condt):
        self.conditions.pop(condt)
    
    def ageUp(self):
        if self.age<4:
            self.age+=1
    
    def changeName(self,newName):
        self.name=newName
    
    def __repr__(self):
        return self.name
    
class player(person):
    def __init__(self,name,age):
        super().__init__(name,age)
        player.inventory = {'Oxen':0,'Wheels':0,'Tongues':0,'Axles':0, 'Ammo':0, 'Food':0,'Clothes':0,'Water':0}
        player.profession = None
        player.currency = 0 #change this perhaps? upon initialization this should be random or hella if ur in godmode
    
    def alterCurrency(self,amount):
        newCurr = self.currency+amount
        if newCurr>=0: #ie valid currency change
            self.currency=newCurr
            return True
        else:
            print("ur broke lol")
            return None
    
    def alterInv(self,item,amount):
        potentialAmt = self.inventory[item]+amount
        if potentialAmt < 0:
            print("Can't do that!")
            return None
        else:
            self.inventory[item] = potentialAmt
            return True

#helper function for getting HP/Stamina values
def getHPStamByAge(age):
    hpStam = 50
    if age<=2:
        hpStam+=150*age
    elif age==3:
        hpStam=300
    elif age==4:
        hpStam=150
    return hpStam
        

#lowkey might want to move ts but this is fine for now
def generateParty(app):
    app.playerParty.append(app.player)
    if app.godmode==True:
        app.playerParty.append(person("",2)) # 1 young adult
    elif app.hardMode==True:
        for i in range(5):
            app.playerParty.append(person("",0)) #5 children
    else:
        partyNumb = randrange(1,6)
        for i in range(partyNumb):
            age = randrange(5)
            app.playerParty.append(person("",age))
    print(app.playerParty)


def drawHPStamBars(app):
    app.playerParty
    drawRect(0,0,app.width,app.height/3+20,fill="lightGray") 
    drawLabel("Party Stats", app.width//2, 12.5,size=15,bold=True,align="bottom")
    drawLine(25,20,app.width-25,20,fill="black",lineWidth=1)
    for i in range(len(app.playerParty)):
        drawHPStamCell(app,i)
    
def drawHPStamCell(app,i):
    partyMemb = app.playerParty[i]
    boldOrNot = True if i==0 else False
    percentHP, percentStam = partyMemb.health/getHPStamByAge(partyMemb.age),partyMemb.health/getHPStamByAge(partyMemb.age) 
    row, col = i//3, i%3
    cellLX, cellTY = 25+125*col,33+57*row
    drawLabel(f'{app.playerParty[i].name}',cellLX+2.5,cellTY+2.5,align="top-left",size=12,bold=boldOrNot,fill="gray")
    drawRect(cellLX,cellTY+17,100*percentHP,15,fill="green") #hp bar itself
    drawRect(cellLX,cellTY+34.5,100*percentStam,15,fill="yellow") #stamina bar itself
    drawRect(cellLX,cellTY+17,100,15,fill=None,border="gray") #hp bar outline
    drawRect(cellLX,cellTY+34.5,100,15,fill=None,border="gray") #stamina bar outline
    if partyMemb.status=="dead":
        drawLine(cellLX,cellTY,cellLX+100,cellTY+50,fill="red")


def drawInv(app):
    drawRect(0,153,app.width,187,fill="sienna")
    drawLabel("Inventory", app.width//2, 167, size=15,bold=True,align="bottom")
    drawRect(50,167+7.5,300,150,fill=None,border="black")
    drawCircle(375,175,20,fill="yellow",border="black")
    drawLabel(f'${app.player.currency}.00',375,175,size=10)
    gridStart=50
    gridLength=350
    itemsList = ["Oxen","Wheels","Tongues", "Axles","Food","Water","Clothes", "Ammo"]
    for i in range(len(itemsList)):
         row, col = i//4, i%4
         cellLX, cellTY = 57.5+75*col,182.5+75*row
         drawRect(cellLX,cellTY,60,60,fill=None,border="black")
         drawLabel(f'{itemsList[i]}',cellLX+30,cellTY+30,align="center")
         drawLabel(f'x{app.player.inventory[itemsList[i]]}',cellLX+55,cellTY+5,align="top-right",bold=True)



def playerDeath(app):
    pass