
from cmu_graphics import *

#========================================================
#BUTTON CLASS
#========================================================

#Note: This code is grounded in what Lauren coded in lecture on Tuesday April 21st.
class button:
    def __init__(self,leftX,topY,width,height,fn,label,color,border="black",textSize=16):
        self.lX = leftX
        self.tY = topY
        self.width = width
        self.height = height
        self.label = label
        self.color = color
        self.fn = fn
        self.borderCol = border
        self.tSize = textSize
    
    def draw(self):
        cX, cY = self.lX+self.width//2, self.tY + self.height//2
        drawRect(self.lX, self.tY, self.width, self.height,fill=self.color,border=self.borderCol)
        drawLabel(self.label, cX,cY,bold=True,size=self.tSize)
    
    def isIn(self,xCoord,yCoord):
        rX,bY = self.lX+self.width, self.tY+self.height
        return (self.lX<=xCoord<=rX) and (self.tY<=yCoord<=bY)
        
    def runFn(self,app):
        self.fn(app)


#========================================================
#PLAYER AND PERSON CLASSES
#========================================================
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
            if self.health+hpStamChange<=getHPStamByAge(self.age):
                self.health+=hpStamChange
            else:
                self.health=getHPStamByAge(self.age)
        elif hpVsStam=="stam":
            if self.stamina+hpStamChange<=getHPStamByAge(self.age):
                self.stamina+=hpStamChange
            else:
                self.stamina=getHPStamByAge(self.age)

    def addCondition(self,condt):
        self.conditions.append(condt)
    
    def removeCondition(self,condt):
        self.conditions.remove(condt)
    
    def ageUp(self):
        if self.age<4:
            self.age+=1
    
    def changeName(self,newName):
        self.name=newName
    
    def checkDeath(self):
        if self.health<=0:
            return "no health"
        elif self.stamina<=0:
            return "exhaustion"

    def __repr__(self):
        return self.name
    
class player(person):
    def __init__(self,name,age):
        super().__init__(name,age)
        player.inventory = {'Oxen':0,'Wheels':0,'Tongues':0,'Axles':0, 'Ammo':0, 'Food':0,'Clothes':0,'Water':0}
        player.profession = None
        player.currency = 0 
    
    def alterCurrency(self,amount):
        newCurr = self.currency+amount
        if newCurr>=0: #ie valid currency change
            self.currency=newCurr
            return True
        else:
            return None
    
    def alterInv(self,item,amount):
        potentialAmt = self.inventory[item]+amount
        if potentialAmt < 0:
            return None
        else:
            self.inventory[item] = potentialAmt
            return True
#small pnp helper function for getting HP/Stamina values
def getHPStamByAge(age):
    hpStam = 50
    if age<=2:
        hpStam+=150*age
    elif age==3:
        hpStam=300
    elif age==4:
        hpStam=150
    return hpStam
 

#========================================================
#LANDMARK CLASS
#========================================================
class landmark:
    def __init__(self,name,mileage):
        self.name=name
        self.miles=mileage


#========================================================
#CONDITION CLASS
#========================================================
class condition:
    def __init__(self,condtName,hpOrStam,phase):
        self.name = condtName
        self.hpOrStam = hpOrStam
        self.phase = 0
    def progressCondt(self):
        self.phase+=1
    def __repr__(self):
        return self.condtName 