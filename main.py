install cmu_graphics
from cmu_graphics import *
def onAppStart(app):
	app.width = 800
	app.height = 600
def redrawAll(app):
  drawLabel("Garden Tycoon", app.width / 2, app.height / 2, size=30, fill="blue")
