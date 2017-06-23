import random,pygame,color
pygame.init()
win = pygame.display.set_mode((600,600))
h = 600

i = 0
cash = 0
win.fill(color.white)
scale = 100

while i < h*scale:
    n = random.randrange(2)

    if n % 2 == 0:
        cash = cash + 1
    else:
        cash = cash - 1

    i = i + 1

    # plot cash at time i//scale
    win.set_at((i//scale, h//2-cash), color.black)

    pygame.draw.line(win, color.red, (0,h//2), (h-1,h//2))
    pygame.display.update()
