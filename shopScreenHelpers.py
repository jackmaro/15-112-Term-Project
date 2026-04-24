from cmu_graphics import *

def drawShop(app,shopName,pricesDict):
    drawRect(0,0,app.width,app.height/3+20,fill="burlyWood") #approx 153
    drawLabel(f"{shopName}", app.width//2, 15,size=20,bold=True,align="bottom")
    drawLine(0,20,app.width,20,fill="black",lineWidth=1)
    itemsList = ["Oxen","Wheels","Tongues", "Axles","Food","Water","Clothes", "Ammo"]
    itemsMeasure = ["yoke","wheel","tongue","axle","pound","liter","set","20"]
    for i in range(len(itemsList)):
         row, col = i//4, i%4
         cellLX, cellTY = 50+85*col,30+60*row
         drawRect(cellLX,cellTY,80,50,fill=None,border="black")
         drawLabel(f'{itemsList[i]}',cellLX+5,cellTY+5,align="top-left",size=10)
         drawLabel(f'''${pricesDict[itemsList[i]]} per {itemsMeasure[i]}''',cellLX+5,cellTY+40,align="left",size=10)         


