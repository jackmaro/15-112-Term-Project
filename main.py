from cmu_graphics import *
from screens import *

def main():
    runAppWithScreens(initialScreen="gameStartScreen")
    
def onAppStart(app):
    app.width=400
    app.height=400
    

main()
