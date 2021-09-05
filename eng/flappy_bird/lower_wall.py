import pygame
from pygame.sprite import Sprite

import game_func as gf


class LowerWall(Sprite):
    def __init__(self, settings):
        """Initializes the settings for the bottom wall."""
        Sprite.__init__(self)

        self.settings = settings
        self.height = 0
        # Load the image and set the frame.
        self.image = pygame.transform.scale(pygame.image.load('./img/models/walls/lower_wall.png'), (100, self.height))
        self.rect = self.image.get_rect()

    def update_image(self):
        """Updates the image to the desired height."""
        self.image = pygame.transform.scale(pygame.image.load('./img/models/walls/lower_wall.png'), (100, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        """Updates the position of the bottom wall on the screen."""
        self.rect.x -= self.settings.walls_speed