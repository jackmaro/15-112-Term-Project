from cmu_graphics import *

def drawInv(app):
    drawRect(0,153,app.width,187,fill="sienna")
    drawLabel("Inventory", app.width//2, 167, size=15,bold=True,align="bottom")
    drawRect(50,167+7.5,300,150,fill=None,border="black")
    drawCircle(375,175,20,fill="yellow",border="black")
    drawLabel(f'${app.player.currency}.00',375,175,size=10)
    gridStart=50
    gridLength=350
    itemsList = ["Oxen","Wheels","Tongues", "Axles","Food","Water","Clothes", "Ammo"]
    for i in range(len(itemsList)):
         row, col = i//4, i%4
         cellLX, cellTY = 57.5+75*col,182.5+75*row
         drawRect(cellLX,cellTY,60,60,fill=None,border="black")
         drawLabel(f'{itemsList[i]}',cellLX+30,cellTY+30,align="center")
         drawLabel(f'x{app.player.inventory[itemsList[i]]}',cellLX+55,cellTY+5,align="top-right",bold=True)
