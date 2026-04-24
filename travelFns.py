from buttonClass import *
from personAndPlayer import *
from conditions import *
from survivalHelpers import *
import math

#THIS IS WHAT I'M WORKING ON NOW
def dayPass(app):
    foodConsumed = app.foodRations*len(app.playerParty)
    app.milesTraveled+= math.floor(getTruePace(app))
    #feeding folks
    if app.player.inventory["Food"]<foodConsumed:
        app.player.inventory["Food"]=0
        #applyPartyDamage(app,5)
    else:
        app.player.alterInv("Food",-foodConsumed)

    #need to add water

    #need to add roll for illness / new condition

    #need new temperature (if time)
