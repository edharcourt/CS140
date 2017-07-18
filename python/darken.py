import pygame, util
pygame.init()

image = pygame.image.load("../images/bug.jpg")
win = pygame.display.set_mode((image.get_width(), image.get_height()))
image = image.convert_alpha()

for y in range(image.get_height()):
    for x in range(image.get_width()):
        (r,g,b,a) = image.get_at((x,y))
        r = r * .7
        g = g * .7
        b = b * .7
        image.set_at((x,y), (r,g,b))

win.blit(image, (0,0))
pygame.display.update()
util.wait_for_click()
