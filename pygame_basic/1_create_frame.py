import pygame

pygame.init() # initalization

# size of display
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title of screen
pygame.display.set_caption("Ian Game")

# even loop
running = True # Is game running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit() # pygame ends