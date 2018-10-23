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
paddle_dy = height // 2 # paddle moves down screen in two seconds

def move(x, y, dx, dy):

    x += dt * ball_dx
    y += dt * ball_dy

    if x + ball_w >= width:     # right wall
        x = width - ball_w
        dx = -dx

    if y < 0:                   #top wall
        y = 0
        dy = -dy
    elif y + ball_h >= height:  # bottom wall
        y = height - ball_h
        dy = -dy

    # check if particle hits paddle.
    if x <= paddle_x + paddle_w and \
       paddle_y <= y <= paddle_y + paddle_h:
        dx = -dx

    return (x,y,dx,dy)

clock = pygame.time.Clock()
pygame.key.set_repeat(1,1)

while True:
    win.fill(color.lightgray)

    dt = clock.tick(60) / 1000.0

    (ball_x,ball_y,ball_dx,ball_dy) = \
          move(ball_x,ball_y,ball_dx,ball_dy)

    # check to see if we lost.
    if ball_x < 0:
        pygame.quit()
        exit()

    event = pygame.event.poll()
    # handle events
    #for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            paddle_y = paddle_y - dt*paddle_dy
        elif event.key == pygame.K_DOWN:
            paddle_y = paddle_y + dt*paddle_dy

    win.blit(ball, (ball_x, ball_y))
    win.blit(paddle, (paddle_x, paddle_y))

    pygame.display.update()
