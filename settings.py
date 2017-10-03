# game options/settings
from os import path

INTRO_TITLE = "DOOM KINGDOM"
TITLE = "Zombie"
WIDTH = 800
HEIGHT = 600
FPS = 60
game_folder = path.dirname(__file__)


# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8

#Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)
LIGHT_BLACK = (60, 60, 55)
DOWN_RED = (216, 40, 35)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
