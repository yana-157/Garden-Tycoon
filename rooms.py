class Store:
	def __init__(self):
		self.rooms = dict()
		self.currentRoom = None
	def addRoom(self, room):
		self.rooms[room.name] = room
	def switchRoom(self, roomName):
		if roomName in self.rooms:
			self.currentRoom = roomName
	def draw(self):
		self.currentRoom.draw()

class Room:
	def __init__(self, name)
		self.name = name
		self.objectRoles = {}
		self.app = app
	def addObject(self, obj, action=None, requiredLevel=0):
		self.objectRoles[obj] = (action, requiredLevel)
	def handleClick(self, obj, playerLevel):
		action, requiredLevel = self.objectRoles[obj]
		if playerLevel >= requiredLevel:
			action()
		else:
			print ('f{action} is locked. Reach {requiredLevel} to unlock!')
