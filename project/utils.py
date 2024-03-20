import pygame


def drawText(screen,text, x, y, size=30, color=(255, 0, 0), font_type = "Comic Sans MS"):
	text = str(text)
	font = pygame.font.SysFont(font_type, size)
	surface = font.render(text, True, color)
	text_width, text_height = font.size(text)
	screen.blit(surface, (x-text_width/2, y-text_height/2))


def resetCursor():
	pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
