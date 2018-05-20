import pygame
import random, util

pygame.init()

# random side length
side = random.randrange(400,800)
win = pygame.display.set_mode((side,side))

# define colors we need
black = (0,0,0)
white = (255,255,255)

# make the backgrond white
pygame.draw.rect(win, white, (0,0,side,side))

# top left
pygame.draw.circle(win, black, (side//4,side//4), side//4,1)

# top right
pygame.draw.circle(win, black, (3*side//4,side//4), side//4,1)

# lower left
pygame.draw.circle(win, black, (side//4,3*side//4), side//4,1)

# lower right
pygame.draw.circle(win, black, (3*side//4,3*side//4), side//4,1)

pygame.display.update()
util.wait_for_click()