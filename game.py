import pygame
import random

#Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SIZE = (700, 500)
CAPTION = "My Game"

#init
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(CAPTION)
done = False
clock = pygame.time.Clock()
x = 10
y = 10
width = 100
x_speed = 4
y_speed = 3

#game loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    x = x + x_speed       
    if x + width > SIZE[0]:
        x_speed = -x_speed
        width = random.randint(40,140)
        x = SIZE[0] - width
    
    if x < 0:
        x_speed = -x_speed
        width = random.randint(40,140)
        x = 0
        
    y = y + y_speed       
    if y + width > SIZE[1]:
        y_speed = -y_speed
        width = random.randint(40,140)
        y = SIZE[1] - width
    
    if y < 0:
        y_speed = -y_speed
        width = random.randint(40,140)
        y = 0

    screen.fill(WHITE)
    # --- Drawing code should go here
    pygame.draw.rect(screen, RED, [x,y,width,width])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()