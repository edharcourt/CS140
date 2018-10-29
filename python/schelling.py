import pygame, random, color, util

def randomly_populate():
    for y in range(grid.get_height()):
        for x in range(grid.get_width()):
            r = random.random()
            if r < .33:
                grid.set_at((x, y), color.blue)
            elif r < .66:
                grid.set_at((x, y), color.green)
            else:
                grid.set_at((x, y), color.white)

def count_like_neighbors(x,y,c):
    like = 0
    nc = 0
    for row in range(y-1, y+2):
        for col in range(x-1, x+2):
            (r,g,b,_) = grid.get_at((row % n, col % n))
            if (r,g,b) != color.white:
                nc = nc + 1
            if (r,g,b) == c:
                like = like + 1

    if nc == 0:
        return 0
    else:
        return (like-1)/nc

def find_empty():
    # keep looking for an empty cell
    # until we find one
    while True:
        x = random.randrange(grid.get_width())
        y = random.randrange(grid.get_height())
        (r,g,b,_) = grid.get_at((x,y))
        if (r,g,b) == color.white:
            return (x,y)


# M a i n    P r o g r a m
pygame.init()
n = 300
grid = pygame.display.set_mode((n,n))
randomly_populate()

done = False

while not done:
    moved = 0
    for y in range(grid.get_height()):
        for x in range(grid.get_width()):
            (r,g,b,_) = grid.get_at((x,y))

            # only move if cell is not empty
            if (r,g,b) != color.white:
                like = count_like_neighbors(x,y,(r,g,b))

                # move if less than half my neighbors
                # are like me
                if like < .6:
                    (ex,ey) = find_empty()
                    grid.set_at((ex,ey), (r,g,b))
                    grid.set_at((x,y), color.white)
                    moved = moved + 1

    pygame.display.update()
    print(moved)
    pygame.event.poll()
    done = (moved == 0)

util.wait_for_click()
#pygame.image.save(grid, "D:/Shared/images/schelling_50_25_50_25.jpg")
