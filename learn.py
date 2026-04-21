from cmu_graphics import *
from main import *
from screens import *



def learnMore(app,learnKey):
    learningTidBit = app.learnDict.get(learnKey,"Nothing to Learn!")
    setActiveScreen("learnScreen")
