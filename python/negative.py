import pygame, util,random
pygame.init()

image = pygame.image.load("../images/bug.jpg")
win = pygame.display.set_mode((image.get_width(), image.get_height()))
image = image.convert_alpha()

for y in range(image.get_height()):
    for x in range(image.get_width()):
        (r,g,b,a) = image.get_at((x,y))
        #image.set_at((x, y), (255 - r, 255 - g, 255 - b))
        image.set_at((x,y), (g,b,r))

win.blit(image, (0,0))
pygame.display.update()
pygame.image.save(image, "D:/Shared/images/gbr_bug.jpg")
util.wait_for_click()
