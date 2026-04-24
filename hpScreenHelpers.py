from cmu_graphics import *
from otClasses import *

def drawHPStamBars(app):
    app.playerParty
    drawRect(0,0,app.width,app.height/3+20,fill="lightGray") 
    drawLabel("Party Stats", app.width//2, 12.5,size=15,bold=True,align="bottom")
    drawLine(25,20,app.width-25,20,fill="black",lineWidth=1)
    for i in range(len(app.playerParty)):
        drawHPStamCell(app,i)
    
def drawHPStamCell(app,i):
    partyMemb = app.playerParty[i]
    boldOrNot = True if i==0 else False
    percentHP, percentStam = partyMemb.health/getHPStamByAge(partyMemb.age),partyMemb.health/getHPStamByAge(partyMemb.age) 
    row, col = i//3, i%3
    cellLX, cellTY = 25+125*col,33+57*row
    drawLabel(f'{app.playerParty[i].name}',cellLX+2.5,cellTY+2.5,align="top-left",size=12,bold=boldOrNot,fill="gray")
    drawRect(cellLX,cellTY+17,100*percentHP,15,fill="green") #hp bar itself
    drawRect(cellLX,cellTY+34.5,100*percentStam,15,fill="yellow") #stamina bar itself
    drawRect(cellLX,cellTY+17,100,15,fill=None,border="gray") #hp bar outline
    drawRect(cellLX,cellTY+34.5,100,15,fill=None,border="gray") #stamina bar outline
    if partyMemb.status=="dead":
        drawLine(cellLX,cellTY,cellLX+100,cellTY+50,fill="red")
