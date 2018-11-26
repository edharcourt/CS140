# Go through an image pixel by pixel.
# If the red component is odd then color
# pixel black. Otherwise color it white.
import pygame, util, color

pygame.init()

#image = pygame.image.load("D:/Shared/images/png/yummy_secret.png")
image = pygame.image.load("../images/png/red_panda_secret.png")
#image = pygame.image.load("T:/Harcourt/gallery/png/church.png")

win = pygame.display.set_mode((image.get_width(),
                               image.get_height()))

win.blit(image, (0,0))
pygame.display.update()

# Go through an image row by row, column by column.
for y in range(win.get_height()):
    for x in range(win.get_width()):
        (r,g,b,_) = win.get_at((x, y))
        if r % 2 == 1:
            win.set_at((x, y), color.black)
        else:
            win.set_at((x, y), color.white)
    pygame.display.update()
    pygame.time.delay(5)

util.wait_for_click()