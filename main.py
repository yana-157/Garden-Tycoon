from cmu_graphics import *
from room import Store
from room import Rooms

def onAppStart(app):
    app.store = Store()
    app.height = 600
    app.width = 800
    app.Room.currentRoom = 'lobby'
    app.playerLevel = 0
    lobby = Room("Lobby")


def redrawAll(app):
    app.Room.currentRoom
    drawImage(app.url, )

def onMousePress(app, mouseX, mouseY):
    app.store.currentRoom.handleClick("object", app.playerLevel)

runApp()
