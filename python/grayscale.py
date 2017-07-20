import pygame, util
pygame.init()

image = pygame.image.load("../images/bug.jpg")
win = pygame.display.set_mode((image.get_width(), image.get_height()))
image = image.convert_alpha()

for y in range(image.get_height()):
    for x in range(image.get_width()):
        (r, g, b, a) = image.get_at((x, y))
        gray = (r + g + b) // 3
        image.set_at((x, y), (gray, gray, gray))

win.blit(image, (0,0))
pygame.display.update()
pygame.image.save(image, "D:/Shared/images/gray_bug.jpg")
util.wait_for_click()
