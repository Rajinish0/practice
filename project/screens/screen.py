from handlers import GameStateMgr

class Screen:
	main = None
	gameMgr = GameStateMgr()

	@staticmethod
	def setMain(main):
		Screen.main = main
	
	def __init__(self):
		pass

	def handleEvent(self, event):
		pass

	def update(self):
		pass

	def draw(self, display):
		pass