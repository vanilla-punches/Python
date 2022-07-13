import os
import pygame
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

# Creating balls
ball_images = [
    pygame.image.load(os.path.join(image_path, "ballon1.png")),
    pygame.image.load(os.path.join(image_path, "ballon2.png")),
    pygame.image.load(os.path.join(image_path, "ballon3.png")),
    pygame.image.load(os.path.join(image_path, "ballon4.png"))]

# Ball speed by size
ball_speed_y = [-18, -15, -12, -9]

# Balls
balls = []

balls.append({
    "pos_x" : 50, # x axis
    "pos_y" : 50, # y axis
    "img_idx" : 0, # image index
    "to_x" : 3, # x axis movement, -3 left, 3 right
    "to_y" : -6, # y axis movement
    "init_spd_y" : ball_speed_y[0]}) # initial speed for y

# Weapon that will disappear and ball
weapon_to_remove = -1
ball_to_remove = -1

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

    # Define Ball's location
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size  = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # When balls hit the wall(width), bouncing back ---> changing its moving direction
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # Bouncing up when it hits the stage
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. Collision

    # character rect info update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # rect info update
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # Collison between character and ball
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # Collison between weapon and ball
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # weapon rect() info update
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # Collison check
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx
                break

    # Removing ball and weapon after collision
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 5. Draw on screen
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() # repeat drawing background

pygame.quit() # pygame ends