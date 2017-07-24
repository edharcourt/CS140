
#
# A function that returns a new scaled image from an
# original image passed to it.  The returned image
# will have dimensions new_widht and new_height.
#
def scale(original, scaled_w, scaled_h):

    scaled = pygame.Surface((scaled_w, scaled_h))
    w_ratio = original.get_width() / scaled_w
    h_ratio = original.get_height() / scaled_h

    for row in range(scaled_h):
        for col in range(scaled_w):
            x = int(col * w_ratio)
            y = int(row * h_ratio)
            (r,g,b,_) = original.get_at((x,y))
            scaled.set_at((col,row), (r,g,b))

    return scaled

# M A I N
import pygame, util,color
pygame.init()

image = pygame.image.load("../images/rainbow_toad_small.jpg")
win = pygame.display.set_mode((image.get_width() * 3, image.get_height() * 3))
#image = image.convert_alpha()
win.blit(image, (0,0))

scaled_image = scale(image, image.get_width() * 3,
                     image.get_height() * 3)

win.blit(scaled_image, (0,0))

pygame.display.update()
util.wait_for_click()

#pygame.image.save(win, "D:/Shared/images/rainbow_toad_enlarged.png")

