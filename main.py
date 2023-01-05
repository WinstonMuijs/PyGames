import pygame
import sys

from pygame import Rect
from pygame.rect import RectType

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
spaceship_rec = spaceship.get_rect(center=(WIDOW_WIDTH/2, WINDOW_HEIGHT/2))
# laser
laser = pygame.image.load('graphics/laser.png').convert_alpha()
laser_rec = laser.get_rect(midbottom=(spaceship_rec.midtop))
# background
background = pygame.image.load('graphics/background.png').convert()

# import text
font = pygame.font.Font('graphics/subatomic.ttf', 50)
text = font.render("Galaxy", True, "seagreen1")
text_rec = text.get_rect(center=(WIDOW_WIDTH/2, WINDOW_HEIGHT-50))

# drawing rectangle

# Keeps the game running in a loop
while True:
    # 1. input of the player(keyboard, mouse, press button,..)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # quits the game
            sys.exit()

        # inputs
        # if event.type == pygame.MOUSEMOTION:
        #     spaceship_rec = event.pos

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("shoot")

    # frame rate
    clock.tick(120)

    # mouse input
    # set ship on mouse position
    spaceship_rec = pygame.mouse.get_pos()

    # 2. updates, layers of the game, orders matter
    display_surface.fill((0, 0, 0))  # display_surface
    display_surface.blit(background, (0, 0))  # background

    # if spaceship_rec.top > 0:  # if spaceship at top of window, stop movement
    #     spaceship_rec.y -= 4  # movement per cycle or iteration of the while loop
    laser_rec.y -= 10  # movement laser

    # positioning surface, drawing images and control movement
    display_surface.blit(text, text_rec)
    display_surface.blit(laser, laser_rec)

    # pygame.draw.rect()
    pygame.draw.rect(display_surface, 'purple',
                     text_rec.inflate(30, 30), width=8, border_radius=5)

    display_surface.blit(spaceship, spaceship_rec)

    # test.fill("navy")             # surface
    # # placing
    # display_surface.blit(test, (880, 360))  # positioning the surface on the display

    # 3. Show the frame/surface to the player
    pygame.display.update()
