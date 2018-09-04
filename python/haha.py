import pygame, color, math
pygame.init()

side = 400
pygame.init()
win = pygame.display.set_mode((side,side))

pygame.draw.circle(win, color.yellow, (200,200), 200)
pygame.draw.arc(win, color.black, (50,50,300,300), math.pi, 2*math.pi, 150)

pygame.draw.ellipse(win, color.red, (125,275,150,75))
pygame.draw.line(win, color.black, (80,120), (160,140),5)
pygame.draw.line(win, color.black, (80,160), (160,140),5)
pygame.draw.line(win, color.black, (400-80,120), (400-160,140),5)
pygame.draw.line(win, color.black, (400-80,160), (400-160,140),5)


pygame.display.update()
input()
