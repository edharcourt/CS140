import pygame

def wait_for_click():
    print("Waiting for click")
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                done = True
        pygame.time.wait(100)

def linecount(fname):
    f = open(fname)
    count = 0
    for _ in f:
        count = count + 1
    f.close()
    return count
