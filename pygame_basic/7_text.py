import pygame

pygame.init() # initalization

# size of display
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title of screen
pygame.display.set_caption("Ian Game")

# FPS
clock = pygame.time.Clock()

# background image load
background = pygame.image.load("/Users/ianlee/Desktop/MMF/Python/pygame_basic/background.JPG")

# loading a character
character = pygame.image.load("/Users/ianlee/Desktop/MMF/Python/pygame_basic/character.JPG")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

# character speed
character_speed = 0.6

# Enemy
enemy = pygame.image.load("/Users/ianlee/Desktop/MMF/Python/pygame_basic/enemy.JPG")
enemy_size = character.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# Font
game_font = pygame.font.Font(None, 40) # font and size

# Total time
total_time = 10

# Time count
start_ticks = pygame.time.get_ticks()


# event loop
running = True # Is game running?
while running:
    dt = clock.tick(60) # frame per second
    # print("fps: " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # checking if key is typed
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # collision setup
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # collison check
    if character_rect.colliderect(enemy_rect):
        print("Collison")
        running = False
        
    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) # drawing background
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # enemy

    # Timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # time is ms, so multiply by 1000 to make seconds 

    # Output word, word color
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # If time is lower than 0, then  game is over
    if total_time - elapsed_time <- 0:
        print("Time over")
        running = False

    pygame.display.update() # repeat drawing background


pygame.time.delay(2000) # wait for 2 seconds before ending
pygame.quit() # pygame ends