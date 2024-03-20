import pygame
from functools import cache
from utils import resetCursor


class Singleton:

	_instance = None
	
	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance._init()
		return cls._instance
	def _init(self):
		assert False, "_init needs to be implemented"

class GameStateMgr(Singleton):
	def _init(self):
		self.curState = None
		self.prevState = None

	def setState(self, state):
		resetCursor()
		self.prevState = self.curState
		self.curState = state
	
	def getState(self):
		return self.curState

	def getPrevState(self):
		return self.prevState

class EventMgr(Singleton):
	def _init(self):
		self.mousePressed = False
	
	def setMousePressed(self, t):
		self.mousePressed = True

	def reset(self):
		self.mousePressed = False

class ImageHandler(Singleton):
	
	def _init(self):
		pass

	@cache	
	def load(self, img, dimensions):
		w, h = dimensions
		img = pygame.image.load(img)
		img = pygame.transform.scale(img, (w, h))
		return img	
	
