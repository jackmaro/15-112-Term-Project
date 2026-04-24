from cmu_graphics import *
from cmu_cpcs_utils import rounded
from travelFns import *


class button:
    def __init__(self,leftX,topY,width,height,fn,label,color,border="black",textSize=16):
        self.lX = leftX
        self.tY = topY
        self.width = width
        self.height = height
        self.label = label
        self.color = color
        self.fn = fn
        self.borderCol = border
        self.tSize = textSize
    
    def draw(self):
        cX, cY = self.lX+self.width//2, self.tY + self.height//2
        drawRect(self.lX, self.tY, self.width, self.height,fill=self.color,border=self.borderCol)
        drawLabel(self.label, cX,cY,bold=True,size=self.tSize)
    
    def isIn(self,xCoord,yCoord):
        rX,bY = self.lX+self.width, self.tY+self.height
        return (self.lX<=xCoord<=rX) and (self.tY<=yCoord<=bY)
        
    def runFn(self,app):
        self.fn(app)

class landmark:
    def __init__(self,name,mileage):
        self.name=name
        self.miles=mileage

def getNearestLM(app):
    currClosest = landmark(None,None)
    for lm in app.landmarks:
        if lm.miles<app.milesTraveled:
            continue
        else:
            if (currClosest.miles==None) or lm.miles<currClosest.miles:
                currClosest = lm
    return currClosest

def drawTravelScreenTop(app):
    drawRect(0,0,app.width,150,fill="skyBlue")
    drawCircle(0,0,40,fill="yellow")
    drawRect(0,130,app.width,20,fill="green")
    #drawImage(app.man,app.manX,50)

#fix animate man later
def animateMan(app):
    app.manX-=10
    if app.manX==-50:
        app.manX=app.width+50

def drawTravelScreenBottom(app):
    drawRect(0,160,app.width,240,fill="burlyWood")
    drawRect(0,150,app.width,10,fill="saddleBrown")
    drawLine(0,150,app.width,150,fill="black",lineWidth=1)
    drawLine(0,160,app.width,160,fill="black",lineWidth=1)
    drawLabel(f"Days on Trail: {app.days} days",12.5,180,size=20,align="left-top")
    drawLabel(f"Miles Left on Trail: {app.milesOfTrail-app.milesTraveled} miles",12.5,210,size=20,align="left-top")
    drawLabel(f"Next Landmark: {getNearestLM(app).name}",12.5,240,size=20,align="left-top")
    drawLabel(f"Miles to Next Landmark: {getNearestLM(app).miles-app.milesTraveled} miles",12.5,270,size=20,align="left-top")
    drawLabel(f"Food Remaining: {app.player.inventory["Food"]} lbs",12.5,300,size=20,align="left-top")
    drawLabel(f"Water Remaining: {app.player.inventory["Water"]} liters",12.5,330,size=20,align="left-top")
    #drawLine(app.width//2,0,app.width//2,app.height,fill="black")
    for butt in app.travelButtons:
        butt.draw()