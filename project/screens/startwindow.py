from button import Button
from constants import *
from .screen import Screen
import os

class StartWindow(Screen):
	def __init__(self):
		self.btn = Button(W/2, H/2, 100, 100, callBack = lambda: self.gameMgr.setState( MAIN_WINDOW ), img = os.path.join (IMG_PATH, 'start.png')  )

	def update(self):
		self.btn.update()

	def draw(self, display):
		display.fill((255, 255, 255))
		self.btn.draw(display)