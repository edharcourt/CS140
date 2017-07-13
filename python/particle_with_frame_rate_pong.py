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

# properties of the paddle
paddle = pygame.image.load("../images/paddle.png")
paddle_w = paddle.get_width()
paddle_h = paddle.get_height()
paddle_x = 10
paddle_y = height // 2 - paddle_h // 2
paddle_dy = 1

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
pygame.key.set_repeat(1,1)

while True:
    win.fill(color.lightgray)

    (ball_x,ball_y,ball_dx,ball_dy) = move(ball_x,ball_y,ball_dx,ball_dy)

    # handle events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle_y = paddle_y - paddle_dy
                paddle_dy = paddle_dy*1.05
            elif event.key == pygame.K_DOWN:
                paddle_y = paddle_y + paddle_dy
                paddle_dy = paddle_dy * 1.05
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle_dy = 1
            elif event.key == pygame.K_DOWN:
                paddle_dy = 1

    win.blit(ball, (ball_x, ball_y))
    win.blit(paddle, (paddle_x, paddle_y))

    pygame.display.update()
