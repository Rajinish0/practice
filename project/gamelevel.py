from constants import game_elements
from constants.game_constants import *
from gameobjects import *
import pygame, pickle, os

def loadKeys():
	with open(os.path.join(RSRC_PATH, 'keycfg.pkl'), 'rb' ) as f:
		keys = pickle.load(f)
	return keys

def init(map_, bw, bh):
	gameobjs = []
	players  = []
	keys = loadKeys()
	for i in range(NUM_BOXES):
		L = []
		for j in range(NUM_BOXES):
			elem = None
			match map_[i][j]:
				case game_elements.BOX:  
					elem = Box(j*bw, i*bh, bw, bh);
				case game_elements.WALL: 
					elem = Wall(j*bw, i*bh, bw, bh);
				case game_elements.PLAYER1:
					players.append(Player(j*bw, i*bh, bw, bh, keys['p1'], img=os.path.join(IMG_PATH, 'p1.png') ))
					elem = Empty(j*bw, i*bh, bw, bh)
				case game_elements.PLAYER2:
					players.append(Player(j*bw, i*bh, bw, bh, keys['p2'], img=os.path.join(IMG_PATH, 'p2.png')))
					elem = Empty(j*bw, i*bh, bw, bh)
				case _:
					elem = Empty(j*bw, i*bh, bw, bh);
			L.append(elem)
		gameobjs.append(L)
	return (gameobjs, players)

class GameLevel:
	def __init__(self, mp, boxwidth, boxheight):
		self.gameobjs, self.players = init(mp, boxwidth, boxheight)
		self.bw = boxwidth
		self.bh = boxheight
		GameObject.setLevel(self)

	def update(self):
		for i in range(NUM_BOXES):
			for j in range(NUM_BOXES):
				self.gameobjs[i][j].update()
		for player in self.players:
			player.update()

	def draw(self, display):
		for i in range(NUM_BOXES):
			for j in range(NUM_BOXES):
				pygame.draw.rect(display, (255, 0, 0), (j*self.bw, i*self.bh, self.bw, self.bh), 1)
				self.gameobjs[i][j].draw(display)

		for player in self.players:
			player.draw(display)
