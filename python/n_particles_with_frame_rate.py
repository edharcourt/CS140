import pygame, color, random, math
pygame.init()
side = 600
win = pygame.display.set_mode((side,side))
width = win.get_width()
height = win.get_height()

ball = pygame.image.load("../images/ball.png").convert_alpha()
ball_w = ball_h = ball.get_width()
r = ball_w//2

x = []
y = []
dx = []
dy = []

for row in range(r, side, 6*r):
    for col in range(r, side, 6*r):
        x.append(col)
        y.append(row)

        # generate random velocities
        tdx = side / (random.random() * 4 + 4)
        tdy = side / (random.random() * 4 + 4)
        if random.random() < .5:
            tdx = -tdx

        if random.random() < .5:
            tdy = -tdy

        dx.append(tdx)
        dy.append(tdy)

"""
win.fill(color.lightgray)
for i in range(len(x)):
    win.blit(ball, (x[i], y[i]))
pygame.display.update()
"""

# compute the distance between two particles
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def move(x, y, dx, dy):

    x += dt * dx
    y += dt * dy

    if x < 0:
        x = 0
        dx = -dx
    elif x + ball_w >= width:
        x = width - ball_w
        dx = -dx

    if y < 0:
        y = 0
        dy = -dy
    elif y + ball_h >= height:
        y = height - ball_h
        dy = -dy

    return (x,y,dx,dy)

# main animation loop
clock = pygame.time.Clock()

while True:
    win.fill(color.lightgray)
    dt = clock.tick(60) / 1000.0

    for i in range(len(x)):
        (x[i],y[i],dx[i],dy[i]) = move(x[i],y[i],dx[i],dy[i])
        win.blit(ball, (x[i], y[i]))

    for i in range(len(x) - 1):
        for j in range(i+1, len(x)):
            if distance(x[i] + r, y[i] + r, x[j] + r, y[j] + r) < 2 * r:
                (dx[i], dx[j]) = (dx[j], dx[i])
                (dy[i], dy[j]) = (dy[j], dy[i])

    pygame.display.update()
    pygame.event.poll()

