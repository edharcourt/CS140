
#
# A function that returns a new scaled image from an
# original image passed to it.  The returned image
# will have dimensions new_widht and new_height.
#
def scale(original, scaled_w, scaled_h):

    scaled = pygame.Surface((scaled_w, scaled_h))
    w_ratio = original.get_width() // scaled_w
    h_ratio = original.get_height() // scaled_h

    for row in range(scaled_h):
        for col in range(scaled_w):
            x = col * w_ratio
            y = row * h_ratio
            (r,g,b,_) = original.get_at((x,y))
            scaled.set_at((col,row), (r,g,b))

    return scaled

# M A I N
import pygame, util,color
pygame.init()

image = pygame.image.load(
    "../images/bug.jpg")

# call our new scale function
scaled_image = scale(image, image.get_width()//3,
                     image.get_height()//3)

win = pygame.display.set_mode((image.get_width(), image.get_height()))
win.blit(image, (0,0))

win.blit(scaled_image, (win.get_width()//2 - scaled_image.get_width()//2,
                        win.get_height()//2 - scaled_image.get_height()//2))

pygame.display.update()
util.wait_for_click()

'''
# slide image in from left
for i in range(win.get_width() - scaled_image.get_width()):
    win.fill(color.white)
    win.blit(scaled_image, (0, 0))
    win.blit(scaled_image,
             (i, win.get_height() -
                 scaled_image.get_height()))
    pygame.display.update()
    pygame.time.delay(10)
'''
#pygame.image.save(win, "D:/Shared/images/big_in_a_bug.png")

