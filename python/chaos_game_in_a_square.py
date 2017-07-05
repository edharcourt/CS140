import pygame, random, color
side = 500
win = pygame.display.set_mode((side,side))

x0 = side // 2 # top middle
y0 = 0

x1 = 0    # left middle
y1 = side//2

x2 = side//2   # bottom middle
y2 = side - 1

x3 = side - 1    # right middle
y3 = side//2

x = random.randrange(side)
y = random.randrange(side)
xx = random.randrange(side)
yy = random.randrange(side)
win.fill(color.white)

t1prev = -1
t2prev = -2

while True:

    # choose a random tower but not the same one as before.
    t = random.randrange(4)
    while t == t1prev:
        t = random.randrange(4)
    t1prev = t

    if (t == 0):
        x = (x + x0) // 2
        y = (y + y0) // 2
    elif (t == 1):
        x = (x + x1) // 2
        y = (y + y1) // 2
    elif t == 2:
        x = (x + x2) // 2
        y = (y + y2) // 2
    else:
        x = (x + x3) // 2
        y = (y + y3) // 2

    # choose a random tower but not the same one as before.
    t = random.randrange(4)
    while t == t2prev:
        t = random.randrange(4)
    t2prev = t

    if (t == 0):
        xx = (xx + x0) // 2
        yy = (yy + y0) // 2
    elif (t == 1):
        xx = (xx + x1) // 2
        yy = (yy + y1) // 2
    elif t == 2:
        xx = (xx + x2) // 2
        yy = (yy + y2) // 2
    else:
        xx = (xx + x3) // 2
        yy = (yy + y3) // 2

    win.set_at((x, y), color.blue)
    win.set_at((xx, yy), color.red)
    pygame.display.update()
