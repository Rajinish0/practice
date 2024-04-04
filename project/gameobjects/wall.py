from .gameobject import GameObject
from constants.game_constants import *
import os

class Wall(GameObject):
	image = os.path.join(IMG_PATH, 'wall.jpg')
