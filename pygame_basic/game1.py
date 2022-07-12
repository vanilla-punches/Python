import pygame
import random
################################################################################################################
# Initialization (Codes must be done)
pygame.init() # initalization

# size of display
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title of screen
pygame.display.set_caption("Game 1")

# FPS
clock = pygame.time.Clock()

################################################################################################################
# 1. Background, Game image(characters), Location, Speed, Font
background = pygame.image.load("/Users/ianlee/Desktop/MMF/Python/pygame_basic/background.jpg")

# Creating a character
character = pygame.image.load("/Users/ianlee/Desktop/MMF/Python/pygame_basic/pika.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# Movement
to_x = 0
character_speed = 10

# Creating an enemy
enemy = pygame.image.load("/Users/ianlee/Desktop/MMF/Python/pygame_basic/sword.jpg")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10


# Event loop
running = True # Is game running?
while running:
    dt = clock.tick(60) # frame per second
    # print("fps: " + str(clock.get_fps()))

    # 2. Event operations(keyboard, mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    # 3. Game character location
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 4. Collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = character.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("Collision between character and enemy")
        running = False

    # 5. Draw on screen
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() # repeat drawing background

pygame.quit() # pygame ends