import color, pygame, random

pygame.init()
win = pygame.display.set_mode((500,100))
side = 500
radius = side//20
px = radius
py = 100//2
win.fill(color.white)

# move particle to the right
while px+radius < side:
    pygame.draw.circle(win, color.blue, (px,py), radius)
    px = px + 2*radius

pygame.display.update()
pygame.image.save(win, "d:/Shared/images/particles.png")
input("Enter")


# move particle to bottom
while py + radius < side:
    win.fill(color.white)
    pygame.draw.circle(win, color.blue, (px,py), radius)
    pygame.display.update()
    pygame.time.delay(5)

    py = py + 1

while px > radius:
    win.fill(color.white)
    pygame.draw.circle(win, color.blue, (px, py), radius)
    pygame.display.update()
    pygame.time.delay(5)
    px = px - 1

# move particle to top
# to do

#cs140.wait_for_quit()



# M a i n    P r o g r a m
# d = cs140.distance(362,498,0,0)
# print(d)

# print(cs140.distance(10,20,90,2000))