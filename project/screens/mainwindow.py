from .screen import Screen
from button import Button 
from constants import *
import pygame

class MainWindow(Screen):
	def __init__(self):
		self.MapMenu = Button(W/2, H/2 - 150, 50, 50, text="Maps", color=GREEN)
		self.CntrlMenu = Button(W/2, H/2 - 50, 50, 50, text="Controls", color=GREEN)
		self.LvlEditor = Button(W/2, H/2 + 50, 50, 50, text="Editor", color=GREEN, callBack= lambda: self.gameMgr.setState(LEVEL_EDITOR) )
		self.ExitButton = Button(W/2, H/2 + 150, 50, 50, text="Exit", color=GREEN, callBack=lambda: pygame.quit())
	
	def update(self):
		self.MapMenu.update()
		self.CntrlMenu.update()
		self.LvlEditor.update()
		self.ExitButton.update()
	
	def draw(self, display):
		display.fill((0, 0, 255))
		self.MapMenu.draw(display)
		self.CntrlMenu.draw(display)
		self.LvlEditor.draw(display)
		self.ExitButton.draw(display)
