import pygame, random, color, util

def randomly_populate(grid):
    for y in range(grid.get_height()):
        for x in range(grid.get_width()):
            r = random.randrange(3)
            if r == 0:
                grid.set_at((x, y), color.blue)
            elif r == 1:
                grid.set_at((x, y), color.green)
            else:
                grid.set_at((x, y), color.white)
