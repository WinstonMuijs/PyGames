import pygame
import sys

# movement and removing laser from list
def laser_update(storage, speed=300):
    for rec in storage:
        rec.y -= speed * dt   # for the movement laser out of list
        if rec.bottom < 0:    # removes laser not inside the window out of list
            storage.remove(rec)

# using time for the score
def display_score():
    score_text = f'Score: {pygame.time.get_ticks()//1000}'
    text = font.render(score_text, True, "seagreen1")
    text_rec = text.get_rect(center=(WIDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
    display_surface.blit(text, text_rec)
    pygame.draw.rect(display_surface, 'purple',
                     text_rec.inflate(30, 30), width=8, border_radius=5)

# game initiate
pygame.init()
WIDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WIDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Galaxy Shooter")
clock = pygame.time.Clock()  # limit max frame rate
# create a surface
# test = pygame.Surface((400, 100))
# We need to attach the surface to the display_surface -blit methode

# importing images&text
# converting for optimizing

# spaceship
spaceship = pygame.image.load('graphics/ship.png').convert_alpha()
# creating rectangles for placing and movement
spaceship_rec = spaceship.get_rect(center=(WIDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
print(type(spaceship_rec))
# background
background = pygame.image.load('graphics/background.png').convert()

# laser import
laser = pygame.image.load('graphics/laser.png').convert_alpha()
laser_storage = []
# laser_rec = laser.get_rect(midbottom = spaceship_rec.midtop)

# import text
font = pygame.font.Font('graphics/subatomic.ttf', 50)

# drawing rectangle

# Keeps the game running in a loop
while True:
    # 1. input of the player(keyboard, mouse, press button,..)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quits the game
            sys.exit()
        # player input, shooting the laser
        if event.type == pygame.MOUSEBUTTONDOWN:  # 0.5 seconds of delay before we can shoot again.
            laser_rect = laser.get_rect(midbottom=spaceship_rec.midtop)
            laser_storage.append(laser_rect)
    # frame rate
    dt = clock.tick(120) / 1000  # Delta Time in seconds instead of ms, so divided by 1000.
    # dT makes it possible that the speed is constant on very computer while playing the game.

    # mouse input
    # set ship on mouse position
    spaceship_rec.center = pygame.mouse.get_pos()

    # 2. updates, layers of the game, orders matter
    display_surface.fill((0, 0, 0))  # display_surface
    display_surface.blit(background, (0, 0))  # background

    # update laser, movement laser
    laser_update(laser_storage)
    # update laser score:
    display_score()
    # positioning surface, drawing images and control movement

    for rect in laser_storage:
        display_surface.blit(laser, rect)

    display_surface.blit(spaceship, spaceship_rec)

    # 3. Show the frame/surface to the player
    pygame.display.update()
