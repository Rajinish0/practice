from handlers import *


class GameObject:
	level = None
	imgHandler = ImageHandler()
	eventMgr = EventMgr()
	image = None
	def __init__(self, x, y, bw, bh):
		self.x = x
		self.y = y
		self.img = self.imgHandler.load(self.image, (bw, bh)) if self.image is not None else None
	def update(self):
		pass
	def draw(self, display):
		if self.img is not None:
			display.blit(self.img, (self.x, self.y))
	@staticmethod
	def setLevel(level):
		GameObject.level = level
