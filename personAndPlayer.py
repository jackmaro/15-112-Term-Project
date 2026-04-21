import random
from main import *

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age #for age, 0=child,1=teenager, 2=young adult, 3=adult, 4=old folk; has hp ramifications
        self.health = getHPStamByAge(self.age)
        self.happiness = 100
        self.stamina = getHPStamByAge(self.age)
        self.conditions = []

    def alterHPStam(self,hpVStam,hpStamChange):
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
    def __init__(self):
        super().__init__()
        player.inventory = []
        player.occupation = None
        player.currency = 0 #change this perhaps? upon initialization this should be random or hella if ur in godmode
    


def getHPStamByAge(age):
    hpStam = 50
    if age<=2:
        hpStam+=150*age
    elif age==3:
        hpStam=300
    elif age==4:
        hpStam=150
    return hpStam
        
def generateParty(app):
    if app.godmode==True:
        app.playerParty.append(person("",2)) # 1 young adult
    elif app.hardMode==True:
        for i in range(5):
            app.playerParty.append(person("",0)) #5 children
    else:
        partyNumb = random.randrange(1,6)
        for i in range(partyNumb):
            age = random.randrange(5)
            app.playerParty.append(person("",age))
    print(app.playerParty)