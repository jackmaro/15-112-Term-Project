from cmu_graphics import *
from otClasses import *

def drawShop(app,shopName):
    drawRect(0,0,app.width,app.height/3+20,fill="burlyWood") #approx 153
    drawLabel(f"{shopName}", app.width//2, 15,size=20,bold=True,align="bottom")
    drawLine(0,20,app.width,20,fill="black",lineWidth=1)
    buttonsList = app.currStoreButtons
    pricesDict = app.currPriceDict
    itemsList = ["Oxen","Wheels","Tongues", "Axles","Food","Water"]
    itemsMeasure = ["yoke","wheel","tongue","axle","pound","liter"]
    for i in range(len(itemsList)):
         row, col = i//4, i%4
         cellLX, cellTY = 50+85*col,30+60*row
         drawRect(cellLX,cellTY,80,50,fill=None,border="black")
         drawLabel(f'{itemsList[i]}',cellLX+5,cellTY+5,align="top-left",size=10)
         drawLabel(f'''${pricesDict[itemsList[i]]} per {itemsMeasure[i]}''',cellLX+5,cellTY+40,align="left",size=10)         
    for butt in buttonsList:
         butt.draw()

def makePurchase(player,item,amt,priceDict):
    price = priceDict[item]
    if player.alterCurrency(-1*amt*price)==True:
        player.alterInv(item,amt)
    else:
        print("Nope!")

def sellBack(player,item,amt,priceDict):
    price = priceDict[item]
    if player.alterInv(item,-1*amt)==True:
        player.alterCurrency(price*amt)
    
def generatePriceDict(priceDict):
    newPD = dict()
    for key in priceDict:
        newPD[key]=priceDict[key]+randrange(0,100)
    return newPD


def generateStoreButtons(app):
    priceDict = app.currPriceDict
    oxenAdd = button(92.5,32.5,35,10,makePurchase,[app.player,"Oxen",1,priceDict],"+","red",None)
    oxenSub = button(92.5,43,35,10,sellBack,[app.player,"Oxen",1,priceDict],"-","red",None)
    wheelsAdd = button(177.5,32.5,35,10,makePurchase,[app.player,"Wheels",1,priceDict],"+","red",None)
    wheelsSub = button(177.5,43,35,10,sellBack,[app.player,"Wheels",1,priceDict],"-","red",None)
    tonguesAdd = button(262.7,32.5,35,10,makePurchase,[app.player,"Tongues",1,priceDict],"+","red",None)
    tonguesSub = button(262.7,43,35,10,sellBack,[app.player,"Tongues",1,priceDict],"-","red",None)
    axlesAdd = button(347.7,32.5,35,10,makePurchase,[app.player,"Axles",1,priceDict],"+","red",None)
    axlesSub = button(347.7,43,35,10,sellBack,[app.player,"Axles",1,priceDict],"-","red",None)
    foodAdd = button(92.5,92.5,35,10,makePurchase,[app.player,"Food",10,priceDict],"+","red",None)
    foodSub = button(92.5,103,35,10, sellBack,[app.player,"Food",10,priceDict],"-","red",None)
    waterAdd = button(177.5,92.5,35,10, makePurchase, [app.player,"Water",10,priceDict],"+","red",None)
    waterSub = button(177.5,103,35,10, sellBack, [app.player, "Water",10,priceDict],"-","red",None)
    return [oxenAdd,oxenSub, wheelsAdd, wheelsSub,tonguesAdd,tonguesSub,axlesAdd,axlesSub,foodAdd,foodSub,waterAdd,waterSub]
