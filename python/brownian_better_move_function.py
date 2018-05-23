import pygame, random, color

#
# move a particle with coordinates (x,y) to
# a new random location, one of its eight neighbors.
#
def move(x,y):
    Δx = random.randrange(-1,2)
    x = x + Δx

    Δy = random.randrange(-1,2)
    y = y + Δy

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