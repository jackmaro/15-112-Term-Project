from cmu_graphics import *

def drawOptions(app,optionsList):
    screenLength = app.height-app.height/6
    for i in range(len(optionsList)):
        yCoord = app.height/6 + i*screenLength/len(optionsList)
        drawLabel(f'{i+1}. {optionsList[i]}',10,yCoord,align='left',size=20) #magic number core teehee

def chooseFromOptions(app,optionsList,functionsList,key):
    if key.isalpha(): return None
    elif int(key) in range(1,len(optionsList)+1):
        newKey = int(key)-1
        print(functionsList[newKey][1])
        if type(functionsList[newKey][1])!=list:
            functionsList[newKey][0](app,functionsList[newKey][1])
        else:
            functionsList[newKey][0](app,*functionsList[newKey][1])


