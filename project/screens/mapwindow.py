from button import Button
from constants import *
from .screen import Screen
from .gamewindow import GameWindow
import os, pygame, pickle



class MapWindow(Screen):

	def __init__(self):
		self.loadMaps()
		self.createButtons()

	def loadMaps(self):
		with open(os.path.join(RSRC_PATH, "mapdata.pkl"), 'rb') as f:
			self.maps = pickle.load(f)

	def createButtons(self):
		self.buttons = []
		for i in range(len(self.maps)):
			self.buttons.append(
		Button(W//2, H//2-100+(i*100), 100, 100,
		       text=f"Map {i+1}",
		       callBack = lambda: self.create_cb(i) )
)

	def create_cb(self, mapid):
		self.main.setState(GAME_WINDOW, GameWindow(self.maps[mapid]))
		self.gameMgr.setState(GAME_WINDOW)
	
	def update(self):
		for button in self.buttons:
			button.update()

	def draw(self, display):
		display.fill((51, 51, 151))
		for button in self.buttons:
			button.draw(display)		
