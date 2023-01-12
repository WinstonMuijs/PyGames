import pygame
import sys
import random

# movement and removing laser from list
def laser_update(storage, speed=300):
    for rec in storage:
        rec.y -= speed * dt   # for the movement laser out of list
        if rec.bottom < 0:    # removes laser not inside the window out of list
            storage.remove(rec)


def asteroid_update(asteroid_list, speed=400):
    for asteroid_tuple in asteroid_list:
        directions = asteroid_tuple[1]
        asteroid_rect = asteroid_tuple[0]
        asteroid_rect.center += directions * speed * dt
        if asteroid_rect.top > WINDOW_HEIGHT:
            asteroid_list.remove(asteroid_tuple)


# using time for the score
def display_score():
    score_text = f'Score: {pygame.time.get_ticks()//1000}'
    text = font.render(score_text, True, "seagreen1")
    text_rec = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
    display_surface.blit(text, text_rec)
    pygame.draw.rect(display_surface, 'purple',
                     text_rec.inflate(30, 30), width=8, border_radius=5)


# laser timer

def laser_timer(shoot, duration=500):
    if not shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            shoot = True
    return shoot

# game initiate
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
spaceship_rec = spaceship.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# background
background = pygame.image.load('graphics/background.png').convert()

# laser import
laser = pygame.image.load('graphics/laser.png').convert_alpha()
laser_storage = []

# laser timer
can_shoot = True
shoot_time = None

# import text
font = pygame.font.Font('graphics/subatomic.ttf', 50)

# asteroid import
asteroid = pygame.image.load('graphics/meteor.png').convert_alpha()
asteroid_list = []

# asteroid timer
asteroid_timer = pygame.event.custom_type()
pygame.time.set_timer(asteroid_timer, 500)

# Keeps the game running in a loop
while True:
    # 1. input of the player(keyboard, mouse, press button,..)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quits the game
            sys.exit()
        # player input, shooting the laser
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot: # 0.5 seconds of delay before we can shoot again.
            # laser
            laser_rect = laser.get_rect(midbottom=spaceship_rec.midtop)
            laser_storage.append(laser_rect)
            # timer
            can_shoot = False
            shoot_time = pygame.time.get_ticks() # time when shooting laser

            # asteroid
        if event.type == asteroid_timer:
            # random position
            x_pos = random.randint(-100, WINDOW_WIDTH + 100)
            y_pos = random.randint(-100, -50)

            # random direction asteroids
            direction = pygame.math.Vector2(random.uniform(-0.5, 0.5), 1)

            # creating asteroids and adding to list
            asteroid_rec = asteroid.get_rect(center=(x_pos, -y_pos))
            asteroid_list.append((asteroid_rec, direction))



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
    can_shoot = laser_timer(can_shoot)  # delay in shooting through timer
    # update laser score:
    display_score()
    # asteroid update
    asteroid_update(asteroid_list)

    # collisions asteroids with spaceship
    for asteroid_tuple in asteroid_list:
        if spaceship_rec.colliderect(asteroid_tuple[0]):
            pygame.quit()
            sys.exit()

    # laser asteroid collisions
    for laser_rect in laser_storage:
        for asteroid_tuple in asteroid_list:
            if laser_rect.colliderect(asteroid_tuple[0]):
                asteroid_list.remove(asteroid_tuple)
                laser_storage.remove(laser_rect)

    # positioning surface, drawing images and control movement
    for rect in laser_storage:
        display_surface.blit(laser, rect)

    for as_tuple in asteroid_list:
        display_surface.blit(asteroid, as_tuple[0])

    display_surface.blit(spaceship, spaceship_rec)

    # 3. Show the frame/surface to the player
    pygame.display.update()
