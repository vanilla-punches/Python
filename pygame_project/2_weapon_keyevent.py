import pygame
import os
################################################################################################################
# Initialization (Codes must be done)
pygame.init() # initalization

# size of display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# title of screen
pygame.display.set_caption("Game 2")

# FPS
clock = pygame.time.Clock()

################################################################################################################
# 1. Background, Game image(characters), Location, Speed, Font
current_path = os.path.dirname(__file__) # return current file directory
image_path = os.path.join(current_path, "images") # return images folder

# Creating background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Creating stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # We do this to make the character on top of the stage

# Creating character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# Character movement
character_to_x = 0

# Character speed
character_speed = 5

# Creating weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# Weapon can use multiple times
weapons = []

# Weapon speed
weapon_speed = 10

# Event loop
running = True # Is game running?
while running:
    dt = clock.tick(30) # frame per second
    # print("fps: " + str(clock.get_fps()))

    # 2. Event operations(keyboard, mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: 
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    # 3. Game character location
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Weapon location adjustment
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # Weapon is moving up

    # Weapon will be gone after touching ceiling
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 4. Collision

    # 5. Draw on screen
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() # repeat drawing background

pygame.quit() # pygame ends