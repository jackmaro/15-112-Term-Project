# from main import *
from personAndPlayer import *
#from conditions import *
from cmu_graphics import *
from optionsFns import *

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

