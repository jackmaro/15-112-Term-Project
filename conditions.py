from main import *

class condition:
    def __init__(self,condtName,hpOrStam,phase):
        self.name = condtName
        self.hpOrStam = hpOrStam
        self.phase = 0
    def progressCondt(self):
        self.phase+=1
    def __repr__(self):
        return self.condtName 