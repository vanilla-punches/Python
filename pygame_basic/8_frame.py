import pygame
################################################################################################################
# Initialization (Codes must be done)
pygame.init() # initalization

# size of display
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title of screen
pygame.display.set_caption("Ian Game")

# FPS
clock = pygame.time.Clock()

################################################################################################################
# 1. Background, Game image(characters), Location, Speed, Font

# Event loop
running = True # Is game running?
while running:
    dt = clock.tick(60) # frame per second
    # print("fps: " + str(clock.get_fps()))

    # 2. Event operations(keyboard, mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 3. Game character location

    # 4. Collision

    # 5. Draw on screen

    pygame.display.update() # repeat drawing background

pygame.quit() # pygame ends