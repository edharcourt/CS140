import pygame, random, color

#
# move a particle with coordinates (x,y) to
# a new random location, one of its eight neighbors.
# Also, if the particle goes off the edge have
# it wrap around.
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
x1 = w//2  # start particle in the middle
y1 = h//2
x2 = w//2
y2 = h//2

win.fill(color.white)

while (0 <= x1 < w) and (0 <= y1 < h) or \
      (0 <= x2 < w) and (0 <= y2 < h):
    win.set_at((x1,y1), color.blue)
    win.set_at((x2,y2), color.green)
    (x1,y1) = move(x1,y1)
    (x2,y2) = move(x2,y2)
    pygame.display.update()

