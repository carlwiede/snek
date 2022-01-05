# import libraries
import pygame
import time
import random

snake_speed = 15

# window size
window_x = 720
window_y = 480

# define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# boot pygame
pygame.init()

# set window
pygame.display.set_caption('snek')
game_window = pygame.display.set_mode((window_x, window_y))

# fps controller
fps = pygame.time.Clock()

while True:
    pass