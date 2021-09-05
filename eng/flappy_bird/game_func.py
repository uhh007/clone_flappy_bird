"""Contains all the game features of the Flappy Bird game."""

import pygame
import sys
import random

from upper_wall import UpperWall
from lower_wall import LowerWall
from carrot import Carrot

pygame.mixer.init()


def check_events(settings, bird, stats):
    """Reacts to keystrokes."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(stats)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, bird, stats)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, bird)


def check_keydown_events(event, settings, bird, stats):
    """Checks keystrokes."""
    if event.key == pygame.K_q:
        save_high_score(stats)
        sys.exit()
    if event.key == pygame.K_SPACE:
        if bird.rect.y > 0:
            play_sound('./sounds/wing/wing.wav')
            bird.rect.y -= settings.jump_height
            bird.anim1()


def check_keyup_events(event, bird):
    """Checks the release of keys."""
    if event.key == pygame.K_SPACE:
        bird.anim2()


def update_screen(screen, settings, bird, walls, carrots, sb):
    """Update the screen and draws the last frame."""
    screen.fill(settings.screen_color)
    sb.show_score()
    # Draws a bird, walls and carrots.
    bird.blit_me()
    walls.draw(screen)
    carrots.draw(screen)
    # Draws the last frame.
    pygame.display.flip()


def spawn_walls(settings, bird, walls, carrots, sb, stats):
    """Spawns a row of carrot walls and checks their positions."""
    if len(walls) == 0:
        spawn_upper_walls(settings, walls)
        spawn_carrots(settings, walls, carrots)
        spawn_lower_walls(settings, walls)
    # Will spawn the top and bottom walls if the distance from one pair of walls to the other is correct.
    elif settings.screen_width - list(walls)[-1].rect.x == settings.distance_between_walls[1]:
        spawn_upper_walls(settings, walls)
        spawn_carrots(settings, walls, carrots)
        spawn_lower_walls(settings, walls)
    check_row_of_walls(bird, walls, carrots, sb, stats)


def check_row_of_walls(bird, walls, carrots, sb, stats):
    """Checks if the wall has reached the edge, checks if the wall or carrot has collided with the bird."""
    for wall in walls.copy():
        # Checks for bird collisions with walls.
        if pygame.sprite.spritecollide(bird, walls, False):
            if stats.bird_lives > 0:
                play_sound('./sounds/die/die.wav')
                stats.bird_lives -= 1
                # Clear screen.
                clearing_screen(bird, walls, carrots, sb)
            else:
                # Clear screen and ending the game.
                play_sound('./sounds/die/die.wav')
                clearing_screen(bird, walls, carrots, sb)
                save_high_score(stats)
                stats.game_active = False
        # Removes walls that extend over the edge of the screen.
        if wall.rect.right < 0:
            walls.remove(wall)
        check_carrots(bird, carrots, sb, stats)


def play_sound(path_to_file):
    """Load and play sound."""
    pygame.mixer.music.load(path_to_file)
    pygame.mixer.music.play()


def check_carrots(bird, carrots, sb, stats):
    """Checks if the carrot has reached the edge and touched the bird."""
    for carrot in carrots.copy():
        # Checks the collision of the carrot with the bird.
        if pygame.sprite.spritecollide(bird, carrots, True):
            play_sound('./sounds/point/point.wav')
            stats.score += 1
            sb.prep_score()
            sb.prep_high_score()
        # Removes carrots that have gone off the edge of the screen.
        if carrot.rect.right < 0:
            carrots.remove(carrot)


def save_high_score(stats):
    """Saves the current record score."""
    if stats.score > stats.high_score:
        with open('record.txt', 'w') as record:
            record.write(str(stats.score))


def clearing_screen(bird, walls, carrots, sb):
    """We clean the screen from walls, carrots and put the bird in its starting position."""
    sb.prep_score()
    walls.empty()
    carrots.empty()
    bird.start_pos()


def spawn_carrots(settings, walls, carrots):
    """Spawn carrots."""
    carrot = Carrot(settings)
    # Set location
    carrot.rect.centery = list(walls)[-1].height + settings.distance_between_walls[0] / 2
    carrot.rect.left = settings.screen_width + 10
    carrots.add(carrot)


def spawn_upper_walls(settings, walls):
    """Spawn upper walls."""
    upper_wall = UpperWall(settings)
    # We initialize the height of the walls, then resize the picture to the given height.
    upper_wall.height = random.randint(100, 600)
    upper_wall.update_image()
    # Set location.
    upper_wall.rect.left = settings.screen_width
    upper_wall.rect.top = 0
    # Add to the group.
    walls.add(upper_wall)


def spawn_lower_walls(settings, walls):
    """Spawn lower walls."""
    lower_wall = LowerWall(settings)
    # We initialize the height of the walls, then resize the picture to the given height.
    lower_wall.height = settings.screen_height - settings.distance_between_walls[0] - list(walls)[-1].height
    lower_wall.update_image()
    # Set location.
    lower_wall.rect.left = settings.screen_width
    lower_wall.rect.bottom = settings.screen_height
    # Add to the group.
    walls.add(lower_wall)
