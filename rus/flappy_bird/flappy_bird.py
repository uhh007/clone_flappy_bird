import pygame
from pygame.sprite import Group

from settings import Settings
import game_func as gf
from bird import Bird
from stats import Stats
from scoreboard import Scoreboard


def start_game():
    """Инициализирует экран и запускает игровой цикл."""
    pygame.init()
    settings = Settings()
    # Создаём экран.
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    screen.fill(settings.screen_color)
    pygame.display.set_caption('Flappy Bird')
    # Создаём экземпляр птицы и группы стен и морковок.
    bird = Bird(screen, settings)
    stats = Stats(settings)
    sb = Scoreboard(settings, screen, stats)
    walls = Group()
    carrots = Group()
    while True:
        # Игровой цикл.
        if stats.game_active:
            gf.check_events(settings, bird, stats)
            gf.spawn_walls(settings, bird, walls, carrots, sb, stats)
            bird.update()
            walls.update()
            carrots.update()
        gf.update_screen(screen, settings, bird, walls, carrots, sb)


start_game()
