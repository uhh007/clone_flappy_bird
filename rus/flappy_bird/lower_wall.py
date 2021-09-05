import pygame
from pygame.sprite import Sprite

import game_func as gf


class LowerWall(Sprite):
    def __init__(self, settings):
        """Инициализирует настройки нижней стены."""
        Sprite.__init__(self)

        self.settings = settings
        self.height = 0
        # Загружаем изображение и задаём рамку.
        self.image = pygame.transform.scale(pygame.image.load('./img/models/walls/lower_wall.png'), (100, self.height))
        self.rect = self.image.get_rect()

    def update_image(self):
        """Обновляет изображение под нужную высоту."""
        self.image = pygame.transform.scale(pygame.image.load('./img/models/walls/lower_wall.png'), (100, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        """Обновляет позицию нижней стены на экране."""
        self.rect.x -= self.settings.walls_speed