from cmu_graphics import *


class button:
    def __init__(self,cX,cY,width,height,fn,label,color):
        self.cX = cX
        self.cY = cY
        self.width = width
        self.height = height
        self.label = label
        self.color = color
        self.fn = fn
    
    def draw(self):
        drawRect(self.cX, self.cY, self.width, self.height,fill=self.color,border="black",align="center")
        drawLabel(self.label, self.cX,self.cY,bold=True,size=16)
    
    def isIn(self,xCoord,yCoord):
        lX,rX= self.cX-self.width//2, self.cX+self.width//2
        tY,bY= self.cY-self.height//2, self.cY+self.height//2
        return (lX<=xCoord<=rX) and (tY<=yCoord<=bY)

    def runFn(self,app):
        self.fn(app)