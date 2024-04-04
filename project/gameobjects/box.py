from .gameobject import GameObject
from constants.game_constants import *
import os

class Box(GameObject):
	image = os.path.join(IMG_PATH, 'images.jpg')
