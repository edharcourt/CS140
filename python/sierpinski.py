import pygame, random, color
side = 500
win = pygame.display.set_mode((side,side))

x0 = side // 2  # tower 0 coordinates
y0 = 0

x1 = side - 1   # tower 1 coordinates
y1 = side - 1

x2 = 0          # tower 2 coordinates
y2 = side - 1

x = random.randrange(side) # hiker coordinates
y = random.randrange(side)

win.fill(color.white)

for i in range(100000):

    #choose a tower at random
    t = random.randrange(3)

    # which tower is it?
    if (t == 0):
        x = (x + x0) // 2
        y = (y + y0) // 2
    elif (t == 1):
        x = (x + x1) // 2
        y = (y + y1) // 2
    else:
        x = (x + x2) // 2
        y = (y + y2) // 2

    win.set_at((x, y), color.blue)
    pygame.display.update()

pygame.image.save(win, "D:/Shared/images/sierpinski1.png")