from .gameobject import GameObject
import pygame
class Player(GameObject):
	def __init__(self, x, y, w, h, keys, img):
		super().__init__(x, y, w, h)
		self.img = self.imgHandler.load(img, (w, h))
		self.keys = keys

	def update(self):
		if self.eventMgr.keyPressed:
#			print("YES")
#			keys = pygame.key.get_pressed()
			if self.eventMgr.keyPressed(self.keys['UP']):
				self.y -= 0.1;
			elif self.eventMgr.keyPressed(self.keys['DOWN']):
				self.y += 0.1;
			elif self.eventMgr.keyPressed(self.keys['RIGHT']):
				self.x += 0.1;
			elif self.eventMgr.keyPressed(self.keys['LEFT']):
				self.x -= 0.1;

	def draw(self, display):
		display.blit(self.img, (self.x, self.y))

