import pygame, random, util, color

s = 600
win = pygame.display.set_mode((s,s))
win.fill(color.white)

for y in range(s):
    for x in range(s):
        if random.random() < .42:
            win.set_at((x,y), color.green)

# Simulate a lightning strike
x = random.randrange(s)
y = random.randrange(s)
burning = [(x,y)]
win.set_at(burning[0], color.red)

# while we have trees to burn
while len(burning) > 0:

    new_burning = []

    # for each tree in burning
    i = 0
    for (tx, ty) in burning:
        count = 0  # count burning or white neighbor trees

        # for each neighbor of the burning tree
        for dy in range(-1, 2):
            y = (ty + dy) % s
            for dx in range(-1, 2):
                x = (tx + dx) % s
                (r,g,b,_) = win.get_at((x,y))


                # I call this depth first burning because we just add a new burning
                # tree to the list allowing it t burn other trees befre we go on to
                # one of the older burning trees.
                # is it green?
                if (r,g,b) == color.green and \
                    random.random() < .5:
                    #new_burning.append((x, y))
                    burning.append((x, y))
                    win.set_at((x, y), color.red)
                    pygame.display.update()

                if (r,g,b) == color.red or \
                   (r,g,b) == color.white:
                    count = count + 1

        # remove burnt trees that cant burn any
        # more neighboring trees
        if count == 9:
            burning.remove((tx,ty))
            #burning.pop(i)
            print(i)

        i = i + 1

    # draw the newly burning trees
#    for (bx,by) in new_burning:
#        win.set_at((bx,by), color.red)

    # concatenate the two lists
#    burning = burning + new_burning

    pygame.display.update()


pygame.display.update()

util.wait_for_click()
