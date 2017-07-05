import pygame, random, color
side = 500
win = pygame.display.set_mode((side,side))

x0 = side // 2 # top middle
y0 = 0

x1 = 0    # left middle
y1 = side-1

x2 = side - 1   # bottom middle
y2 = side - 1

x = random.randrange(side)
y = random.randrange(side)
xx = random.randrange(side)
yy = random.randrange(side)
win.fill(color.white)

xx0 = side // 2 # top middle
yy0 = 0

xx1 = 0    # left middle
yy1 = side//2

xx2 = side//2   # bottom middle
yy2 = side - 1

xx3 = side - 1    # right middle
yy3 = side//2


t1prev = -1
t2prev = -2

while True:

    # choose a random tower but not the same one as before.
    t = random.randrange(3)
    #while t == t1prev:
    #    t = random.randrange(4)
    #t1prev = t

    if (t == 0):
        x = (x + x0) // 2
        y = (y + y0) // 2
    elif (t == 1):
        x = (x + x1) // 2
        y = (y + y1) // 2
    elif t == 2:
        x = (x + x2) // 2
        y = (y + y2) // 2

    # choose a random tower but not the same one as before.
    t = random.randrange(4)
    while t == t2prev:
        t = random.randrange(4)
    t2prev = t

    if (t == 0):
        xx = (xx + xx0) // 2
        yy = (yy + yy0) // 2
    elif (t == 1):
        xx = (xx + xx1) // 2
        yy = (yy + yy1) // 2
    elif t == 2:
        xx = (xx + xx2) // 2
        yy = (yy + yy2) // 2
    else:
        xx = (xx + xx3) // 2
        yy = (yy + yy3) // 2

    win.set_at((x, y), color.blue)
    win.set_at((xx, yy), color.red)
    pygame.display.update()
