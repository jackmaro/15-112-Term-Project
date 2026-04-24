from otClasses import *





#========================================================
# Person and Player Special Functions
#========================================================
def applyProfession(app,profession):
    if profession=="Banker":
        app.player.profession="Banker"
        app.player.alterCurrency(800)
        setActiveScreen("partyNamingScreen")
    elif profession=="Carpenter":
        app.player.profession="Carpenter"
        app.player.alterCurrency(400)
        setActiveScreen("partyNamingScreen")
    elif profession=="Farmer":
        app.player.profession="Farmer"
        app.player.alterCurrency(200)
        setActiveScreen("partyNamingScreen")

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

def playerDeath(app):
    pass


#========================================================
# Landmark Special Functions
#========================================================

def getNearestLM(app):
    currClosest = landmark(None,None)
    for lm in app.landmarks:
        if lm.miles<app.milesTraveled:
            continue
        else:
            if (currClosest.miles==None) or lm.miles<currClosest.miles:
                currClosest = lm
    return currClosest

