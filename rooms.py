class Rooms:
	def __init__(self, name):
		self.name = name
			self.objects = []
			self.objectRoles = dict()
			self.playerLevel = playerLevel
	def addObject(self, obj, action=None, requiredLevel=0):
		self.objectRoles[obj] = (action, requiredLevel)
	def handleClick(self, obj):
		if obj in self.objectRoles:
			action, requiredLevel = self.objectRoles[obj]
				if self.playerLevel >= requiredLevel:
					action()
				else:
					print 'f{action} is locked. Reach {requiredLevel} to unlock this feature!}

						

