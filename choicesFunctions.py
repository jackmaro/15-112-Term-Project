# from main import *
from personAndPlayer import *
#from conditions import *
from cmu_graphics import *
from optionsFns import *

def applyProfession(app,profession):
    if profession=="Banker":
        app.player.profession="Banker"
        app.player.alterCurrency(1600)
        print("You're a Banker now!")
        setActiveScreen("partyNamingScreen")
    elif profession=="Carpenter":
        app.player.profession="Carpenter"
        app.player.alterCurrency(800)
        print("You're a Carpenter Now!")
        setActiveScreen("partyNamingScreen")
    elif profession=="Farmer":
        app.player.profession="Farmer"
        app.player.alterCurrency(400)
        print("You're a Farmer now!")
        setActiveScreen("partyNamingScreen")

