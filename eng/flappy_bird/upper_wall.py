import pygame
import random
from pygame.sprite import Sprite

import game_func as gf


class UpperWall(Sprite):

    def __init__(self, settings):
        """Initializes the top wall settings."""
        Sprite.__init__(self)

        self.settings = settings
        self.height = 0
        # Load the image and set the frame.
        self.image = pygame.transform.scale(pygame.image.load('./img/models/walls/upper_wall.png'), (100, self.height))
        self.rect = self.image.get_rect()

    def update_image(self):
        """Updates the image to the required height."""
        self.image = pygame.transform.scale(pygame.image.load('./img/models/walls/upper_wall.png'), (100, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        """Updates the position of the top wall on the screen."""
        self.rect.x -= self.settings.walls_speed