import pygame,util,color
pygame.init()

def make_red_even(image):
    for y in range(image.get_height()):
        for x in range(image.get_width()):
            (r, g, b, _) = image.get_at((x, y))
            if r % 2 == 1:
                image.set_at((x, y), (r - 1, g, b))
    return image


def make_message_surface(msg):
    font = pygame.font.SysFont("Veranda", 80)
    return font.render(msg, False, color.black)

# Main Program
win = pygame.display.set_mode((1,1))
image = pygame.image.load("../images/png/red_panda.png").convert_alpha()

image = make_red_even(image)
msg = make_message_surface("Attack At Dawn")

message_surf = pygame.Surface((image.get_width(), image.get_height()))
message_surf.fill(color.white)
message_surf.blit(msg, (message_surf.get_width()//2 - msg.get_width()//2,
                        message_surf.get_height()//2 - msg.get_height()//2))


for y in range(image.get_height()):
    for x in range(image.get_width()):
        (r,g,b,_) = message_surf.get_at((x,y))
        if (r,g,b) == (0,0,0):
            (ir,ig,ib,_) = image.get_at((x,y))
            image.set_at((x,y), (ir+1,ig,ib))

pygame.image.save(image, "../images/png/red_panda_secret.png")
print("Done")