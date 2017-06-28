import random,pygame,color
pygame.init()
win = pygame.display.set_mode((3200,800))
h = win.get_height()
w = win.get_width()

i = 0
cash = 0
win.fill(color.white)
xscale = 1
yscale = 10
bet = 1

while i < win.get_width()*xscale:
    n = random.randrange(2)

    if n % 2 == 0:
        cash = cash + bet
        bet = 1
    else:
        cash = cash - bet
        bet = bet * 2

    i = i + 1

    # plot cash at time i//scale
    win.set_at((i // xscale, (h // 2 - cash)), color.black)

    pygame.draw.line(win, color.red, (0,h//2), (w-1,h//2))
    pygame.display.update()
input()