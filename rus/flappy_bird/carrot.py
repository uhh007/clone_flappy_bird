import pygame
from pygame.sprite import Sprite


class Carrot(Sprite):
    def __init__(self, settings):
        """Инициализирует морковку."""
        Sprite.__init__(self)

        self.settings = settings
        # Загружаем изображение и ставим рамку.
        self.image = pygame.image.load('./img/models/carrot/carrot.png')
        self.rect = self.image.get_rect()

    def update(self):
        """Обновляет позицию морковки на экране."""
        self.rect.x -= self.settings.walls_speed