[source,python]
----
import pygame, color

# initial pygame stuff
pygame.init()
width = 600   # display surface 600 pixels wide
height = 400  # display surface is 400 pixels high
win = pygame.display.set_mode((width,height))

# create the background
win.fill(color.lightgray)

# set up some variable for the head
head_width = width // 3
head_height = height // 3
head_x = width // 2 - head_width // 2
head_y = height // 2 - head_height // 2
pygame.draw.rect(win, color.yellow, (head_x, head_y, head_width, head_height))

# left eye
left_eye_x = head_x + head_width // 4
left_eye_y = head_y + head_height // 4
left_eye_r = head_width // 2 // 3 // 2  # width of quadrant is r_width//2 then 1/3 of that
pygame.draw.circle(win, color.darkgray, (left_eye_x, left_eye_y), left_eye_r)

# left eye cross
pygame.draw.line(win, color.white,
                 (left_eye_x, left_eye_y - left_eye_r),
                 (left_eye_x, left_eye_y + left_eye_r))

pygame.draw.line(win, color.white,
                 (left_eye_x - left_eye_r, left_eye_y),
                 (left_eye_x + left_eye_r, left_eye_y))

# right eye
right_eye_x = head_x + 3 * head_width // 4
right_eye_y = head_y + head_height // 4
right_eye_r = head_width // 2 // 3 // 2  # width of quadrant is r_width//2 then 1/3 of that
pygame.draw.circle(win, color.darkgray, (right_eye_x, right_eye_y), right_eye_r)

# mouth
mouth_width = head_width // 2
mouth_height = head_height // 4
mouth_x = head_x + head_width // 2 - mouth_width // 2
mouth_y = head_y + 2 * head_height // 3
pygame.draw.ellipse(win, color.pink, (mouth_x, mouth_y, mouth_width, mouth_height))

# smile
pygame.draw.ellipse(win, color.yellow, (mouth_x, mouth_y, mouth_width, mouth_height - .2 * mouth_height))

# add a nose
nose_width = head_width // 10  # 1/10th width of head
nose_height = head_height // 4 # 1/4 height of head
nose_x = head_x + head_width // 2 - nose_width // 2  # centered horizontally
nose_y = head_y + head_height // 2 - nose_height // 2  # centered vertically
pygame.draw.ellipse(win, color.blue, (nose_x, nose_y, nose_width, nose_height))

pygame.display.update()

input("Hit <enter> when done")
include:python/blockhead.py
----
