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
ball_dx = .04
ball_dy = .01

win.fill(color.lightgray)
win.blit(ball, (ball_x, ball_y))
pygame.display.update()

def move(x, y, dx, dy):

    x = x + dx
    y = y + dy

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

while True:
    win.fill(color.lightgray)
    (ball_x,ball_y,ball_dx,ball_dy) = move(ball_x,ball_y,ball_dx,ball_dy)
    win.blit(ball, (ball_x, ball_y))
    pygame.display.update()

input()