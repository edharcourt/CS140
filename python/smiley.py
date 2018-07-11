
# main program
import pygame, random, util, math,color
side = random.randrange(400,600)
pygame.init()
win = pygame.display.set_mode((side,side))
x = 100
# A function to draw a smiley on the
# pygame window win at coordinate
# (x,y) radius r using color.
def draw_smiley(win, clr, x, y, r):
    pygame.draw.circle(win, clr, (x, y), r)

    # properites of the left eye
    # variables defined within the function
    # are called local variables
    lex = x - r//2  # left eye x-coordinate
    ley = y - r//2  # left eye y-coordinate
    lew = r//4      # left eye width
    leh = r//2      # left eye height
    pygame.draw.ellipse(win, color.black, (lex,ley,lew,leh))

    #properties of the right eye
    rex = x + r//4  # right eye x-coordinate
    rey = ley       # right eye y-coordinate is same as left eye
    rew = lew       # ditto width
    reh = leh       # ditto height
    pygame.draw.ellipse(win, color.black, (rex,rey,rew,reh))

    # properties of the smile
    sx = lex       # mouth x-coordinate
    sy = y + r//8  # mouth y-coordinate
    sw = r         # mouth width is oen redius, or half the head
    sh = r//2      # mouth height is 1/4 head or 1/2 radius
    sa = math.pi   # start angle, start at left
    ea = 2*math.pi # end angle, end at right
    pygame.draw.arc(win, color.black, (sx,sy,sw,sh), sa,ea, 4)

#---------------------------------------
# The main program
#---------------------------------------
draw_smiley(win, color.yellow,
            side//2, side//2, side//2)

"""
draw_smiley(win, color.green,
            3*side//4, side//4, side//4)

draw_smiley(win, color.cyan,
            side//4, 3*side//4, side//4)

draw_smiley(win, color.orange,
            3*side//4, 3*side//4, side//4)

r = 30
x = r
y = side//2

# move smiley right
while x + r < side:
    win.fill(color.lightgray)
    draw_smiley(win, color.yellow,
                x, y, r)
    x = x + 1
    pygame.display.update()
    pygame.time.delay(5)

# move smiley up
while y > r:
    win.fill(color.lightgray)
    draw_smiley(win, color.green,
                x, y, r)
    y = y - 1
    pygame.display.update()
    pygame.time.delay(5)

# move smiley to the left
while x > r:
    win.fill(color.lightgray)
    draw_smiley(win, color.green,
                x, y, r)
    x = x - 1
    pygame.display.update()
    pygame.time.delay(5)

# move smiley diagonally to the middle
while x < side//2:
    win.fill(color.lightgray)
    draw_smiley(win, color.green,
                x, y, r)
    x = x + 1
    y = y + 1
    pygame.display.update()
    pygame.time.delay(5)

# make smiley bigger
while r < side//2:
    win.fill(color.lightgray)
    draw_smiley(win, color.green,
                x, y, r)
    r = r + 1
    pygame.display.update()
    pygame.time.delay(5)

"""
pygame.display.update()
pygame.image.save(win,"../images/smiley.png")
