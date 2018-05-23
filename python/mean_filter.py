
#
# Return a color as an RGB triple that represents the average
# color of the neighbord of the pixel at coordinate (x,y).
#
def neighborhood_mean(surf, x, y):

    red_sum = 0
    green_sum = 0
    blue_sum = 0

    for ny in range(y-1,y+2):
        for nx in range(x-1,x+2):
            (r,g,b,_) = surf.get_at((nx,ny))
            red_sum += r
            green_sum += g
            blue_sum += b

    red_avg = int(round(red_sum/9))
    green_avg = int(round(green_sum/9))
    blue_avg = int(round(blue_sum/9))

    return (red_avg, green_avg, blue_avg)

def mean_filter(orig):
    surf = pygame.Surface((orig.get_width(), orig.get_height()))

    for y in range(1,orig.get_height()-1):
        for x in range(1, orig.get_width()-1):
            (r,g,b) = neighborhood_mean(orig, x,y)
            surf.set_at((x,y), (r,g,b))
    return surf

# M A I N
import pygame, util
pygame.init()

image = pygame.image.load("../images/rainbow_toad_enlarged.png")

win = pygame.display.set_mode((image.get_width(), image.get_height()))
win.blit(image, (0,0))
pygame.display.update()

print("Click to continue")
util.wait_for_click()

surf = mean_filter(image)

win.blit(surf, (0,0))

pygame.display.update()

print("Click to continue")
util.wait_for_click()

#pygame.image.save(win, "D:/Shared/images/filtered_toad.png")

