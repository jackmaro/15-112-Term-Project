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
        player.inventory = {'Oxen':0,'Wheels':0,'Tongues':0,'Axles':0, 'Ammo':0, 'Food':0}
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
    #i have 133 to work with. margins vertical are 11. blocks for text+bars=50 so 15 for name + 17 per bar
    startX, startY = 25,11
    party = [app.player]+app.playerParty
    barLength = 100
    barWidth = 35
    for i in range(len(party)):
        barSX = startX+((i+1)//3)*(barLength+25)
        barSY = startY+15+(i%2)*(barWidth+11)
        labelSY =startY+((i+1)//2)*(barWidth)
        midLineY=barSY+17.5
        drawRect(barSX,barSY,barLength,barWidth, fill="lightGray") #hp bar, unfilled
        drawRect(barSX,barSY+17.5,barLength,barWidth, fill="lightGray") #stamina bar, unfilled
        drawLine(barSX,barSY,barSX+barLength,barSY,fill="gray")
        drawLabel(f'{party[i].name}',barSX,barSY,align="left-top",size=15)
        percentHP = party[i].health/getHPStamByAge(party[i].age)
        percentStam = party[i].stamina/getHPStamByAge(party[i].age)
        drawRect(barSX,barSY,barLength*percentHP,barWidth, fill="green") #hp bar, unfilled
        drawRect(barSX,barSY+17.5,barLength*percentStam,barWidth, fill="yellow") #stamina bar, unfilled
    pass

def drawInv(app):
    drawLabel(f'{app.player.currency}',app.width-1,app.height//3+11,align="right-top")
    cX, cY = app.width-22,app.height//3+12
    drawCircle(cX,cY,10,fill="yellow",border="black")
    pass


def playerDeath(app):
    pass