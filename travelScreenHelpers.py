from cmu_graphics import *
from cmu_cpcs_utils import rounded
from travelFns import *
from otClasses import *
from otClassFns import *

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