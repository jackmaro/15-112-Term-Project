from cmu_graphics import *

def learnMore(app,learnKey):
    learningTidBit = app.learnDict.get(learnKey,"Nothing to Learn!")
    setActiveScreen("learnScreen")
