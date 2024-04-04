from button import Button
from constants import *
from .screen import Screen
from gamelevel import GameLevel
import os, pygame



class GameWindow(Screen):
	offSetX = 0
	offSetY = 40
	boxWidth  = (W-offSetX)//NUM_BOXES
	boxHeight = (H-offSetY)//NUM_BOXES

	def __init__(self, map_):
		self.gamelevel = GameLevel(map_, self.boxWidth, self.boxHeight)
		self.gameSurface = pygame.Surface( (W-self.offSetX, H-self.offSetY))

	def update(self):
		self.gamelevel.update()

	def draw(self, display):
		display.fill(BLACK)
		self.gameSurface.fill(BLACK)
		self.gamelevel.draw(self.gameSurface)
		display.blit(self.gameSurface, (self.offSetX, self.offSetY) )

	@staticmethod
	def screentoCoords(x, y):
		return (y//GameWindow.boxHeight, x//boxWidth)
