from cmu_graphics import *

def drawOptions(app,optionsList):
    screenLength = app.height-app.height/6
    for i in range(len(optionsList)):
        yCoord = app.height/6 + i*screenLength/len(optionsList)
        if optionsList[i]!="":
            drawLabel(f'{i+1}. {optionsList[i]}',10,yCoord,align='left',size=20) #magic number core teehee
        else:
            drawLabel(f'{i+1}. <Type Stuff Here!>',10,yCoord,align='left',size=20) #partially for debugging, but also for 


def chooseFromOptions(app,optionsList,functionsList,key):
    #option 1: choose using number inputs
    if key.isalpha(): return None
    elif int(key) in range(0,len(optionsList)+1):
        newKey = int(key)-1
        print(functionsList[newKey][1])
        if type(functionsList[newKey][1])!=list:
            return functionsList[newKey][0](functionsList[newKey][1])
        else:
            return functionsList[newKey][0](*functionsList[newKey][1])
    #option 2: use arrows and enter??

