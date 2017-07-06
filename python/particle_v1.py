import pygame, color
pygame.init()
side = 600
win = pygame.display.set_mode((side,side))

ball = pygame.image.load("../images/ball.png").convert_alpha()
win.fill(color.black)
win.blit(ball, (side//2, side//2))
pygame.display.update()

input()