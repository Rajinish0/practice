from constants.colors import *
from handlers import *
from utils import *
import pygame

def _defHover():
	pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

class Button:
	evMgr = EventMgr()
	imgHandler = ImageHandler()
	hovered = False

	def __init__(self, x, y, width, height, text = None,
			     img = None, color = RED, callBack=None,
			 	 onHover=_defHover, center=True,
				 drawRect = False):
		self.x = x
		self.y = y
		self.w = width
		self.h = height
		self.img = img
		self.color = color
		self.text = text
		self.cb = callBack
		self.onHover = onHover
		self.drawRect = drawRect
		self.pressed = False
		self.hovered = False
		if center: self.centerCords()
	def centerCords(self):
		self.x -= self.w/2
		self.y -= self.h/2	

	def update(self):
		self.pressed = False
		if self.mouseInside():
			if (not self.hovered):
				self.onHover()
				self.hovered = True

			if self.evMgr.mousePressed:
				if self.cb is not None: self.cb()
				self.pressed = True
		elif self.hovered:
			resetCursor()
			self.hovered = False
			
			

	def mouseInside(self):
		(mx, my) = pygame.mouse.get_pos()
		return (mx >= self.x and mx <= self.x + self.w and
			my >= self.y and my <= self.y + self.h)

	def draw(self, display):
		if self.img is not None:
			display.blit(self.imgHandler.load(self.img, (self.w, self.h) ), (self.x, self.y))
		elif self.drawRect:
			pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))
		if self.text is not None:
			drawText(display, self.text, self.x + self.w/2, self.y+self.h/2, size = self.w//2)

