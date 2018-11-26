import pygame, random

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)

def wait_for_quit():
    print("Waiting for quit")
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
        pygame.time.wait(100)


# Randomly populate a grid with blue and green agents.
def randomly_populate():
    for y in range(grid.get_height()):
        for x in range(grid.get_width()):
            r = random.random()
            if r < .33:
                grid.set_at((x, y), blue)
            elif r < .66:
                grid.set_at((x, y), green)
            else:
                grid.set_at((x, y), white)

# count the number of neighbors of (x,y) that are
# like (x,y).
def count_like_neighbors(x,y,c):
    like = 0
    nc = 0
    for row in range(y-1, y+2):
        for col in range(x-1, x+2):
            (r,g,b,_) = grid.get_at((row % n, col % n))
            if (r,g,b) != white:
                nc = nc + 1
            if (r,g,b) == c:
                like = like + 1

    if nc == 0:
        return 0
    else:
        return (like-1)/nc

# Randomly look for an empty cell and return one when found.
def find_empty():
    # keep looking for an empty cell
    # until we find one
    while True:
        x = random.randrange(grid.get_width())
        y = random.randrange(grid.get_height())
        (r,g,b,_) = grid.get_at((x,y))
        if (r,g,b) == white:
            return (x,y)


#########################################################
# M a i n    P r o g r a m
#########################################################
pygame.init()
n = 300
grid = pygame.display.set_mode((n,n))
randomly_populate()

done = False

t = 1/3   # threshold

# Keep agents moving until we are done
while not done:
    moved = 0

    # go through the entire grid once moving agents.
    for y in range(grid.get_height()):
        for x in range(grid.get_width()):
            (r,g,b,_) = grid.get_at((x,y))

            # only move if cell is not empty
            if (r,g,b) != white:
                like = count_like_neighbors(x,y,(r,g,b))

                # move if less than the threshold t
                if like < t:
                    (ex,ey) = find_empty()
                    grid.set_at((ex,ey), (r,g,b))
                    grid.set_at((x,y), white)
                    moved = moved + 1

    pygame.display.update()
    print(moved)
    pygame.event.poll()
    done = (moved == 0)

wait_for_quit()
