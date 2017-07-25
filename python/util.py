import pygame

def wait_for_click():
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                done = True
        pygame.time.wait(100)

