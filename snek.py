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

# define snake default position
snake_position = [100, 50]

# define initial blocks of the body
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]  
            ]

# random fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# default snake direction
direction = 'RIGHT'
change_to = direction

# default score
score = 0

# display score function
def show_score(choice, color, font, size):
    
    # create font object
    score_font = pygame.font.SysFont(font, size)
    
    # display surface object
    score_surface = score_font.render('Score: ' + str(score), True, color)

    # rectangle for surface object
    score_rect = score_surface.get_rect()
    
    # display the text
    game_window.blit(score_surface, score_rect)

# game over
def game_over():
    
    # create font object
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # create text surface
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # rectangle for surface
    game_over_rect = game_over_surface.get_rect()
    
    # set position of text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # draw text
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # display for 5 seconds
    time.sleep(5)
    
    # deactivate pygame
    pygame.quit()
    
    # exit the program
    quit()

while True:
    pass