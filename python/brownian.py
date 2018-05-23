import pygame, random, color

#
# move a particle with coordinates (x,y) to
# a new random location, one of its eight neighbors.
#
def move(x,y):
    dir = random.randrange(1,9)
    if dir == 1:
        y = y - 1
    elif dir == 2:
        x = x + 1
        y = y - 1
    elif dir == 3:
        x = x + 1
    elif dir == 4:
        x = x + 1
        y = y + 1
    elif dir == 5:
        y = y + 1
    elif dir == 6:
        y = y + 1
        x = x - 1
    elif dir == 7:
        x = x - 1
    else:
        x = x - 1
        y = y - 1

    return (x,y)

# main program
pygame.init()

win = pygame.display.set_mode((600,600))
w = win.get_width()
h = win.get_height()
x = w//2  # start particle in the middle
y = h//2

win.fill(color.white)

while (0 <= x < w) and (0 <= y < h):
    win.set_at((x,y), color.blue)
    (x,y) = move(x,y)
    pygame.display.update()

pygame.image.save(win, "d:/Shared/images/brownian.png")
input("Hit enter")