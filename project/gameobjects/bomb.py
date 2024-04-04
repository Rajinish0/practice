from .gameobject import GameObject
from constants.game_constants import *
import os

class Bomb(GameObject):
	image = os.path.join(IMG_PATH, 'bomb.jpg')
