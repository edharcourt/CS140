import pygame, color
pygame.init()
side = 600
win = pygame.display.set_mode((side,side))
width = win.get_width()
height = win.get_height()

ball = pygame.image.load("../images/ball.png").convert_alpha()
ball_w = ball.get_width()
ball_h = ball.get_height()
ball_x = width//2 - ball_w//2
ball_y = height//2 - ball_h//2
ball_dx = width // 2 # across screen in two seconds (units are pixels/second)
ball_dy = height // 4 # down screen in four seconds

def move(x, y, dx, dy):

    dt = clock.tick(60) / 1000.0

    x += dt * ball_dx
    y += dt * ball_dy

    if x < 0:
        x = 0
        dx = -dx
    elif x + ball_w >= width:
        x = width - ball_w
        dx = -dx

    if y < 0:
        y = 0
        dy = -dy
    elif y +ball_h >= height:
        y = height - ball_h
        dy = -dy

    return (x,y,dx,dy)

clock = pygame.time.Clock()

while True:
    win.fill(color.lightgray)

    (ball_x,ball_y,ball_dx,ball_dy) = move(ball_x,ball_y,ball_dx,ball_dy)

    win.blit(ball, (ball_x, ball_y))
    pygame.display.update()
    pygame.event.poll()
