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
    font = pygame.font.SysFont("Veranda", 40)
    return font.render(msg, False, color.black)

# Main Program
image = pygame.image.load("../images/png/yummy.png")

image = make_red_even(image)
msg = make_message_surface("Python is awesome")

for y in range(msg.get_height()):
    for x in range(msg.get_width()):
        (r,g,b,_) = msg.get_at((x,y))
        if (r,g,b) == (0,0,0):
            (ir,ig,ib,_) = image.get_at((x,y))
            image.set_at((x,y), (ir+1,ig,ib))

pygame.image.save(image, "D:/Shared/images/png/yummy_secret.png")
print("Waiting for click to quit")
util.wait_for_click()