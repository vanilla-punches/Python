import pygame

pygame.init() # initalization

# size of display
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title of screen
pygame.display.set_caption("Ian Game")

# background image load
background = pygame.image.load("/Users/ianlee/Desktop/MMF/Python/pygame_basic/background.JPG")

# loading a character
character = pygame.image.load("/Users/ianlee/Desktop/MMF/Python/pygame_basic/character.JPG")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# event loop
running = True # Is game running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) # drawing background
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # repeat drawing background

pygame.quit() # pygame ends

