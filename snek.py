# import libraries
import pygame
import time
import random

snek_speed = 15

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

# define snek default position
snek_position = [100, 50]

# define initial blocks of the body
snek_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]  
            ]

# random fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# default snek direction
direction = 'RIGHT'
next_dir = direction

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

# main
while True:
    
    # handle key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                next_dir = 'UP'
            if event.key == pygame.K_DOWN:
                next_dir = 'DOWN'
            if event.key == pygame.K_LEFT:
                next_dir = 'LEFT'
            if event.key == pygame.K_RIGHT:
                next_dir = 'RIGHT'
    
    # change direction           
    # disallowing 180 degree turns
    if next_dir == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if next_dir == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if next_dir == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if next_dir == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
    # move snek
    if direction == 'UP':
        snek_position[1] -= 10
    if direction == 'DOWN':
        snek_position[1] += 10
    if direction == 'LEFT':
        snek_position[0] -= 10
    if direction == 'RIGHT':
        snek_position[0] += 10
        
    # snek body growing mechanism
    snek_body.insert(0, list(snek_position))
    if snek_position[0] == fruit_position[0] and snek_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snek_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    
    fruit_spawn = True
    
    game_window.fill(black)
    
    for pos in snek_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    
    # game over conditions
    if snek_position[0] < 0 or snek_position[0] > window_x-10:
        game_over()
    if snek_position[1] < 0 or snek_position[1] > window_y-10:
        game_over()
        
    # snek touching itself
    for block in snek_body[1:]:
        if snek_position[0] == block[0] and snek_position[1] == block[1]:
            game_over()
            
    # display score
    show_score(1, white, 'times new roman', 20)
    
    # refresh screen
    pygame.display.update()
    
    # refresh rate
    fps.tick(snek_speed)