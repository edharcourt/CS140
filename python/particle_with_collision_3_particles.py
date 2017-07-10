import pygame, color, math
pygame.init()
side = 400
win = pygame.display.set_mode((side,side))
width = win.get_width()
height = win.get_height()

ball = pygame.image.load("../images/ball.png").convert_alpha()
ball_w = ball.get_width()
ball_h = ball.get_height()
r = ball_w//2

ball1_x = width // 2 - ball_w // 2
ball1_y = height // 2 - ball_h // 2
ball1_dx = width / 2.02 # across screen in two seconds (units are pixels/second)
ball1_dy = height / 3.99 # down screen in four seconds

ball2_x = width // 4 - ball_w // 2
ball2_y = height // 4 - ball_h // 2
ball2_dx = width / 1.1603 # across screen in two seconds (units are pixels/second)
ball2_dy = height / -2.237 # down screen in four seconds

ball3_x = width - ball_w
ball3_y = height // 4 - ball_h // 2
ball3_dx = width / -0.8603 # across screen in two seconds (units are pixels/second)
ball3_dy = height / 1.237 # down screen in four seconds

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def move(x, y, dx, dy):

    dt = clock.tick(60) / 1000.0

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
    elif y +ball_h >= height:
        y = height - ball_h
        dy = -dy

    return (x,y,dx,dy)

clock = pygame.time.Clock()

while True:
    win.fill(color.lightgray)

    (ball1_x, ball1_y, ball1_dx, ball1_dy) = move(ball1_x, ball1_y,
                                                  ball1_dx, ball1_dy)
    (ball2_x, ball2_y, ball2_dx, ball2_dy) = move(ball2_x, ball2_y,
                                                  ball2_dx, ball2_dy)

    (ball3_x, ball3_y, ball3_dx, ball3_dy) = move(ball3_x, ball3_y,
                                                  ball3_dx, ball3_dy)

    # check collision
    if distance(ball1_x + r,
                ball1_y + r,
                ball2_x + r,
                ball2_y + r ) < 2 * r:
        (ball1_dx, ball2_dx) = (ball2_dx, ball1_dx)
        (ball1_dy, ball2_dy) = (ball2_dy, ball1_dy)

    elif distance(ball1_x + r,
                ball1_y + r,
                ball3_x + r,
                ball3_y + r ) < 2 * r:
        (ball1_dx, ball3_dx) = (ball3_dx, ball1_dx)
        (ball1_dy, ball3_dy) = (ball3_dy, ball1_dy)

    elif distance(ball2_x + r,
                ball2_y + r,
                ball3_x + r,
                ball3_y + r ) < 2 * r:
        (ball2_dx, ball3_dx) = (ball3_dx, ball2_dx)
        (ball2_dy, ball3_dy) = (ball3_dy, ball2_dy)



    win.blit(ball, (ball1_x, ball1_y))
    win.blit(ball, (ball2_x, ball2_y))
    win.blit(ball, (ball3_x, ball3_y))
    pygame.display.update()
    pygame.event.poll()
