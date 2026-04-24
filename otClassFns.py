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
        app.playerParty.append(person("",2)) #for debugging
        #partyNumb = randrange(1,6)
        #for i in range(partyNumb):
        #    age = randrange(5)
        #    app.playerParty.append(person("",age))

def partyStatusChange(app,hpOrStam,rateOfRegen,reason=None):
    for folk in app.playerParty:
        folk.alterHPStam(hpOrStam,rateOfRegen)
        if (rateOfRegen<0) and (folk.checkDeath()!=None): #short circuits if gaining health
            if reason!=None:
                applyDeath(app,folk,reason)
            else:
                applyDeath(app,folk,folk.checkDeath())

def applyDeath(app,folk,reason):
    if folk==app.player:
        playerDeath(app,reason)
    else:
        app.puQueue=popUp(f'''{folk} has died of {reason} :( ''')
        app.playerParty.remove(folk)

def playerDeath(app,reason):
    app.deathReason = reason
    setActiveScreen("deathScreen")




#========================================================
# Landmark Special Functions
#========================================================

def getNearestLM(app):
    currClosest = landmark(None,None)
    for lm in app.landmarks:
        if (lm.miles>app.milesTraveled) and ((currClosest.miles==None) or lm.miles<currClosest.miles):
                currClosest = lm
    return currClosest

#========================================================
# Pop-Up Special Functions
#========================================================
