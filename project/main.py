import pygame, sys
from handlers import *
from constants import *
from screens import *

pygame.init()
class Main:
	def __init__(self):
		self.display = pygame.display.set_mode((W, H))
		self.clock = pygame.time.Clock()
		self.run = True
		self.gameMgr = GameStateMgr()
		self.eventMgr = EventMgr()
		self.init()

	def pollEvents(self):
		self.eventMgr.reset()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.eventMgr.setMousePressed(True)
			self.states[self.gameMgr.getState()].handleEvent(event)
	
	def update(self):
		self.states[self.gameMgr.getState()].update()	

	def draw(self):
		self.display.fill(BLACK)
		self.states[self.gameMgr.getState()].draw(self.display)

	def setState(self, name, state):
		self.states[name] = state

	def init(self):
		Screen.setMain(self)
		self.states = {START_WINDOW : StartWindow(), MAIN_WINDOW: MainWindow(), LEVEL_EDITOR: LevelEditor() }
		self.gameMgr.setState( START_WINDOW )

	def mainLoop(self):
		try:
			while self.run:
				self.update()
				self.draw()
				pygame.display.flip()
				self.pollEvents()
		except pygame.error:
			sys.exit()


if __name__ == '__main__':
	main = Main()
	main.mainLoop()
	
