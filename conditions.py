from main import *

class condition:
    def __init__(self,condtName,hpOrStam,stage):
        self.name = condtName
        self.hpOrStam = hpOrStam
        self.stage = 0
    def progressCondt(self):
        self.stage+=1
    def __repr__(self):
        return self.condtName 